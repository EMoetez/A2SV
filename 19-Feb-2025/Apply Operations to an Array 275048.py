# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        i=0
        while i<len(nums)-1:           
            if nums[i]==nums[i+1] and nums[i]!=0:
                res.append(nums[i]*2)
                i+=2
            elif nums[i]!=0:
                res.append(nums[i])
                i+=1
            else:
                i+=1

        if nums[-1]!=nums[-2] and nums[-1]!=0:
            res.append(nums[-1])
            return res+[0]*(len(nums)-len(res))
        else:
            return res+[0]*(len(nums)-len(res))

