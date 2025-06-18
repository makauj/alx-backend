import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error('Redis error:', err);
});

client.on('connect', () => {
  console.log('Connected to Redis');
});

await client.connect();

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value);
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}

await displaySchoolValue('ALX');
await setNewSchool('ALXSanFrancisco', '100');
await displaySchoolValue('ALXSanFrancisco');
