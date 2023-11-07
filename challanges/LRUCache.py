from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # An ordered dictionary to maintain LRU order

    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end (most recently used position)
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move the item to the end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is full, remove the least recently used item (the first item)
                self.cache.popitem(last=False)
            self.cache[key] = value

# Example usage:
cache = LRUCache(2)  # Create an LRU cache with a capacity of 2

cache.put(1, 1)  # Cache is now {1: 1}
cache.put(2, 2)  # Cache is now {1: 1, 2: 2}
print(cache.get(1))  # Output: 1 (value of key 1)
cache.put(3, 3)  # Cache is now {2: 2, 3: 3} (1 is removed because it's the least recently used)
print(cache.get(2))  # Output: 2 (value of key 2)
print(cache.get(1))  # Output: -1 (key 1 is not found)
