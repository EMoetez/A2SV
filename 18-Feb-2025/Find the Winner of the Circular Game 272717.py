# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """        
        q=deque()
        for i in range(1,n+1):
            q.append(i)

        while len(q)>1:
            for i in range(k-1):    
                q.append(q.popleft())
            q.popleft()
            
        return q[0]
                




            

