# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        h_map={}
        for index,v in enumerate(nums):
            h_map[v]=index
        
        for old,new in operations:
            h_map[new]=h_map[old]
            del h_map[old]
        
        for value, index in h_map.items():
            nums[index]=value
        return nums
