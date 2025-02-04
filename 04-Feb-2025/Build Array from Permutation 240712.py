# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=nums[0]
        b=nums[nums[0]]
        meta=a+len(nums)*b
        for i in range(len(nums)):
            a=nums[i]
            b=(nums[a])%len(nums)
            meta=a+len(nums)*b
            nums[i]=meta
        for i in range(len(nums)):
            nums[i]=nums[i]//len(nums)
        return nums