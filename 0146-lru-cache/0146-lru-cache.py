from collections import defaultdict, deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict()
        self.capacity = capacity
        self.order = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) == self.capacity:
            evicted_key = self.order.popleft()
            del self.cache[evicted_key]
        self.order.append(key)
        self.cache[key] = value
