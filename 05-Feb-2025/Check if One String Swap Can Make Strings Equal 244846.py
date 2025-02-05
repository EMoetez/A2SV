# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        swap=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                swap+=1
        coll1=Counter(s1)
        coll2=Counter(s2)
        
        return coll1==coll2 and swap<=2