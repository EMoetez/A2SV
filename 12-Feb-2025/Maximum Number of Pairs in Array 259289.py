# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        removed=0
        pairs=0
        for i in range(len(nums)):
            
            if nums[i] in nums[i+1:] and nums[i]!=-1:
                
                tmp=nums[i]
                nums[i]= -1
                nums[nums.index(tmp)]= -1
                removed+=2
                pairs+=1

        return [pairs,(len(nums)-removed)]

            

