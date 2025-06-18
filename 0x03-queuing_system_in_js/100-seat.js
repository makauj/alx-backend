import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

// --- Redis setup ---
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Initialize available seats and reservation flag
const AVAILABLE_SEATS_KEY = 'available_seats';
let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync(AVAILABLE_SEATS_KEY, number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync(AVAILABLE_SEATS_KEY);
  return seats !== null ? Number(seats) : 0;
}

// --- Initialize seats to 50 at startup ---
(async () => {
  await reserveSeat(50);
})();

// --- Kue queue setup ---
const queue = kue.createQueue();

// --- Express setup ---
const app = express();
const port = 1245;

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});

// GET /available_seats - returns current number of seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats.toString() });
});

// GET /reserve_seat - enqueue a reservation job if reservations enabled
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {});

  job.save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// GET /process - process the queue reserve_seat
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      let seats = await getCurrentAvailableSeats();
      seats = Number(seats);

      const newSeats = seats - 1;

      if (newSeats < 0) {
        done(new Error('Not enough seats available'));
        return;
      }

      await reserveSeat(newSeats);

      if (newSeats === 0) {
        reservationEnabled = false;
      }

      done();
    } catch (error) {
      done(error);
    }
  });
});
