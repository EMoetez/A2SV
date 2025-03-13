# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        occ_sum= 0
        nums.sort()
        left,right=0, len(nums)-1
        while left<right:
            sum_=nums[left]+nums[right]
            if sum_==k:
                occ_sum+=1
                left+=1
                right-=1
            elif sum_ < k:
                left+=1
            else:
                right-=1
        return occ_sum