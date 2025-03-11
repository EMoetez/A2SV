# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return 0
        nums.append(0)
        left_sum,right_sum=0,sum(nums[1:])
        for i in range(n):
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
            right_sum-=nums[i+1]
        return -1