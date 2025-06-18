// server.js
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// ==================== Redis Client (v3.x) ====================

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// ==================== Products ====================

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

// ==================== Redis stock helpers ====================

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// ==================== Express ====================

const app = express();
const port = 1245;

const notFound = { status: 'Product not found' };

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json(notFound);
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const stock = currentStock !== null ? Number(currentStock) : item.initialAvailableQuantity;

  const responseItem = { ...item, currentQuantity: stock };
  res.json(responseItem);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json(notFound);
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) {
    currentStock = item.initialAvailableQuantity;
  } else {
    currentStock = Number(currentStock);
  }

  if (currentStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});
