# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        mapper= dict(zip(indices,s))
        res=[]
        for i in range(len(s)):
            res.append(mapper[i])
        return "".join(res)
