# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(matrix)
        m=len(matrix[0])
        res=[[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i]=matrix[i][j]
        return res