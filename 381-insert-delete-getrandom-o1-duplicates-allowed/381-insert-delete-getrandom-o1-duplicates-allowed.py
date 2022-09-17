class RandomizedCollection:

    def __init__(self):
        self.hashmap = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.hashmap[val].add(len(self.list))
        self.list.append(val)
        return len(self.hashmap[val]) == 1

    '''
    {
    1: (0, 2)
    2: (3)
    3: (1)
    }
    [1, 3, 1, 2]
    last = 3
    idx = 1
    
    '''
    def remove(self, val: int) -> bool:
        if not self.hashmap[val]:
            return False
        last = self.list[-1]
        idx = self.hashmap[val].pop()
        self.list[idx] = last
        self.hashmap[last].add(idx)
        
        self.hashmap[last].remove(len(self.list) - 1)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()