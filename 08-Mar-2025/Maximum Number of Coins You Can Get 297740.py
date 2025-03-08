# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_coins=0
        piles.sort(reverse=True)
        ranges=2* (len(piles)//3)
        
        for i in range(1,ranges+1,2):
            
            max_coins+=piles[i]
        return max_coins

