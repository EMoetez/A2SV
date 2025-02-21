# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet(object):

    def __init__(self):
        self.numbers={}
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.numbers:
            return False  
        else:
            self.numbers[val]=1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.numbers:   
            del self.numbers[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.numbers))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()