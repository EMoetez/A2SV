# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        set_all= set(allowed)
        count=0
        for word in words:
            if set(word).issubset(set_all):
                count+=1
        return count


