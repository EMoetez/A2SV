# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_sum=0
        for row_idx in range(1,len(grid)-1):
            for col_idx in range(1,len(grid[0])-1):
                summ=grid[row_idx][col_idx]+sum(grid[row_idx-1][col_idx-1:col_idx+2])+sum(grid[row_idx+1][col_idx-1:col_idx+2])
                max_sum=max(max_sum,summ)
        return max_sum
