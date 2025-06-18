import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

const KEY = 'ALX';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

for (let i = 0; i < keys.length; i++) {
  await client.hSet(KEY, keys[i], values[i]);
}

const result = await client.hGetAll(KEY);
console.log(result);
