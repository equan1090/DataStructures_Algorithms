class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.random = []

    def insert(self, val: int) -> bool:
        if val not in self.cache:
            self.cache[val] = len(self.random)
            self.random.append(val)
            return True
        return False
    

    def remove(self, val: int) -> bool:
        '''
        {3: 0, 9: 1, 5: 2}
        [3 9 5]
        '''    
        if val in self.cache:
            
            idx = self.cache[val]
            last = self.random[-1]
            self.cache[last] = idx
            self.random[idx] = last
            del self.cache[val]
            self.random.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.random)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()