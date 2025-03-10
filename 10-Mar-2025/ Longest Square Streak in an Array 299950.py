# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        unique=set(nums)
        longest=-1
        curr=1
        for num in nums:
            curr=1
            while num**2 in unique: 
                num=num**2
                curr+=1
            longest=max(longest,curr)

        return longest if longest!=1 else -1
        