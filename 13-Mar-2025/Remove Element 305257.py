# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==val:
                if nums[r]!=val:
                    nums[l],nums[r]=nums[r],nums[l]
                else:
                    r-=1
            else:
                l+=1

        count=0
        i=0
        while i<len(nums):
            if nums[i]!=val:
                count+=1
                i+=1
            else:
                break

        return count
    
