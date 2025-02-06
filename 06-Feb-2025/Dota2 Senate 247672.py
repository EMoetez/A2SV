# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        qd=deque()
        qr=deque()
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=="R":
                qr.append(i)
            else:
                qd.append(i)
        while qd and qr:
            if qd[0]<qr[0]:
                qd.append(n+qd[0])
            else:
                qr.append(n+qr[0])
            qr.popleft()
            qd.popleft()
        return "Radiant" if qr else "Dire"
            
                
                
                


        