# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """        
        count=set()
        last=k-1
        tmp=0
        i=0
        while len(count)<n:          
            if i % n not in count:                
                tmp+=1
            if tmp==k:                
                tmp=0
                last=i%n
                count.add(last)
            i+=1         
        return last+1
                




            

