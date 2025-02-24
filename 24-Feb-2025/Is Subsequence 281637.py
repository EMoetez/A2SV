# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_p,t_p=0,0

        if len(s)==0:
            return True
        if len(s)>len(t):
            return False
        while s_p<len(s) and t_p<len(t):
            if s[s_p]==t[t_p]:
                s_p+=1
                if s_p>=len(s):
                    return True
            t_p+=1
        return False
        


            

        


