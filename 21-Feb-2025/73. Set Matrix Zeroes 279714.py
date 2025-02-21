# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        col=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.add(i)
                    col.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in col or i in rows:
                    matrix[i][j]=0
                
        return matrix