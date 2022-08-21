class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.cache:
            self.cache[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.cache:
            idx = self.cache[val]
            last = self.arr[-1] 
            self.arr[idx] = last
            self.cache[last] = idx
            self.arr.pop()
            del self.cache[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()