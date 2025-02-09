# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])>=valueDifference and abs(i-j)>=indexDifference:
                    return [i,j]
        return [-1,-1]



        # l,r=0,0+indexDifference
        # while r<len(nums):
        #     if abs(nums[l]-nums[r]) >= valueDifference:
        #         return [l,r]
        #     else:
        #         l+=1
        #         r+=1
        # return [-1,-1]
        