from random import randint

class RandomizedSet:

    def __init__(self):
        self.set = []     
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        else:
            self.positions[val] = len(self.set)
            self.set.append(val)
            return True


    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        else:
            position = self.positions.pop(val)
            replace = self.set.pop()
            
            if replace != val:
                self.set[position] = replace
                self.positions[replace] = position
            return True


    def getRandom(self) -> int:
        n = len(self.set)-1
        index = randint(0,n)
        return self.set[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()