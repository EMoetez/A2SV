# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=0
        cycle=set()
        if n==1:
            return True
        while summ not in cycle and n!=1:
            cycle.add(n)
            summ=0
            while n!=0:
                summ+=(n%10)**2
                n=n//10
            n=summ     
        return n==1
                
            
            