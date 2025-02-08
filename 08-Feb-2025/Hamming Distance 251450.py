# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c=0
        num= x^y
        while num!=0 :
            
            c+= num &1
            
            num=num>>1
            
        return c

