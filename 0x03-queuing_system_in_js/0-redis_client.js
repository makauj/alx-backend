import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});
