class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    {1: 0, 5: 1, 9: 2}
    [1, 9]
    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val]
            last = self.arr[-1]
            self.arr[idx] = last
            self.arr.pop()
            self.map[last] = idx
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()