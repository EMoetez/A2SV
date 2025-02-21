# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for row in image:
            tmp= list(map(lambda x: abs(x-1),row))
            tmp.reverse()
            res.append(tmp)
        return res