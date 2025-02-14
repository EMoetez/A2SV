# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen=[]
        res=[]
        for i in nums:
            if i in seen:
                res.append(i)
            else:
                seen.append(i)
        return res 
