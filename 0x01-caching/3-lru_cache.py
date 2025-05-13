#!/usr/bin/env python3
"""LRU cache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and is a caching system
    that follows the Least Recently Used (LRU) policy.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve the item from the cache and update its usage order"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
