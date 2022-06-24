class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value  