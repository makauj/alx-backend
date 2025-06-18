import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

await subscriber.connect();

const CHANNEL = 'ALXchannel'; // Match this with publisher

await subscriber.subscribe(CHANNEL, (message) => {
  console.log(message);

  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(CHANNEL);
    subscriber.quit();
  }
});
