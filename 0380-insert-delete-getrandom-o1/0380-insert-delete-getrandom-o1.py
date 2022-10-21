import random
class RandomizedSet:
    def __init__(self):
        self.dictionary = {}
        self.array = []

    def insert(self, val: int) -> bool:
        # print(self.array, self.dictionary)
        if val in self.dictionary:
            return False
        self.array.append(val)
        self.dictionary[val] = len(self.array) - 1
        # print(self.array)
        # print("---")
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dictionary:
            return False
        # if self.array[-1] == val:
        #     del self.dictionary[val]
        #     self.array.pop()
        #     return True
        temp = self.dictionary[val]
            
        
        last = len(self.array) - 1
        # del self.dictionary[val]          not here
        self.dictionary[self.array[last]] = temp 
        
        swap = self.array[temp]
        self.array[temp] = self.array[last]
        self.array[last] = swap
        self.array.pop()
        del self.dictionary[val]   # this should be here
        # print(self.array, temp)
        return True

    def getRandom(self) -> int:
        x = random.randint(0, len(self.array)-1)
        return self.array[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()