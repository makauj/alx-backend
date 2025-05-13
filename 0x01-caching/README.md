# 0x01-caching

## Learning Objectives

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

Here’s a breakdown of the learning objectives for **0x01-caching**, along with concise explanations for each:

---

### 1. **What a caching system is**

A **caching system** is a high-speed data storage layer that stores a subset of data, typically transient in nature, so that future requests for that data are served faster than accessing the primary storage (like a database or API). It's used to improve performance and reduce latency.

---

### 2. **What FIFO means**

**FIFO** stands for **First-In, First-Out**.
It is a cache eviction policy where the **oldest** entry (the one added first) is removed first when the cache reaches its limit.

🧠 Example:
If items are added in the order A, B, C and the cache is full, adding a new item D will evict A.

---

### 3. **What LIFO means**

**LIFO** stands for **Last-In, First-Out**.
It is a policy where the **most recently added** item is removed first when the cache is full.

🧠 Example:
If items are added A, B, C and the cache is full, adding D will evict C.

---

### 4. **What LRU means**

**LRU** stands for **Least Recently Used**.
This policy evicts the item that **hasn't been accessed in the longest time**.

🧠 Example:
If A, B, and C are in cache, and A hasn’t been used recently, it will be evicted when adding D.

---

### 5. **What MRU means**

**MRU** stands for **Most Recently Used**.
Contrary to LRU, MRU removes the **most recently used item** when the cache is full.

🧠 Example:
If A, B, and C are in the cache, and C was accessed last, C will be evicted when adding D.

---

### 6. **What LFU means**

**LFU** stands for **Least Frequently Used**.
It evicts the item with the **lowest access count** over time.

🧠 Example:
If A has been used 3 times, B once, and C 2 times, B will be evicted when adding D.

---

### 7. **What the purpose of a caching system**

The main goals are:

- Improve **performance** by reducing access time to frequently used data
- Decrease **load** on backend systems (like databases or web services)
- Improve **scalability** of applications

---

### 8. **What limits a caching system has**

Caching systems have several **limitations**:

- **Size**: Limited storage capacity, requiring eviction policies
- **Staleness**: Data can become outdated if not refreshed properly
- **Complexity**: Implementing invalidation and consistency logic
- **Miss Penalty**: If a requested item isn’t in the cache (cache miss), performance can suffer
- **Overhead**: Adds resource usage, especially memory

---
