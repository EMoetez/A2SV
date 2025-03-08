# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist=list(set(nums))
        dist.sort(reverse=True)
        if len(dist)<3:
            return dist[0]
        return dist[2]
