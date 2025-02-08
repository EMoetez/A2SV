# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def to_binary(num):
            res=[]
            while num>0:
                bit = num % 2
                res.append(str(bit))
                num //=2
            res.reverse()
            return "".join(res)

        x_bin=to_binary(x)  
        y_bin=to_binary(y) 

        x_bin="0" * abs(len(x_bin)-len(y_bin)) + x_bin
        y_bin="0" * abs(len(x_bin)-len(y_bin)) + y_bin

        count=0
        for i in range(len(x_bin)):
            if x_bin[i]!=y_bin[i]:
                count+=1
        return count

