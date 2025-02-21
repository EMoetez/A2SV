# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.timeToLive=timeToLive
        self.auth={}

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId not in self.auth:
            self.auth[tokenId]=currentTime

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.auth:
            if currentTime - self.auth[tokenId]>= self.timeToLive:
                del self.auth[tokenId]
            else:
                self.auth[tokenId] = currentTime  

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        count=0
        for time in self.auth.values():
            if currentTime-time<self.timeToLive:
                count+=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)