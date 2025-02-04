# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.de= deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.de.append(t)
        while self.de[0]<t-3000:
            self.de.popleft()

        return len(self.de)


        




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)