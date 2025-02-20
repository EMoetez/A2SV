# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        d = {}  
        res = []  
        reverse = True  
        for i in range(len(mat)):
            for j in range(len(mat[0])):  
                if i + j in d:
                    d[i + j].append(mat[i][j])
                else:
                    d[i + j] = [mat[i][j]]

        for i in range(len(mat) + len(mat[0]) - 1):  
            if reverse:
                res.extend(d[i][::-1])  
            else:
                res.extend(d[i])  
            reverse = not reverse  
        return res
