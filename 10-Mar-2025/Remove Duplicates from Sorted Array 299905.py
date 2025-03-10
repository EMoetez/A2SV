# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=[nums[0]]
        curr=nums[0]
        for i in nums:
            if i!=curr:
                unique.append(i)
                curr=i
        k=len(unique)
        for i in range(k):
            nums[i]=unique[i]
        nums[k:]='_'
        return k


