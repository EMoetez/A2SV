# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)