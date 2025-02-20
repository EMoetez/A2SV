# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for ni in range(i - 1, i + 2):  
                    for nj in range(j - 1, j + 2): 
                        if 0 <= ni < m and 0 <= nj < n: 
                            total += img[ni][nj]
                            count += 1
                result[i][j] = total // count 
        
        return result
