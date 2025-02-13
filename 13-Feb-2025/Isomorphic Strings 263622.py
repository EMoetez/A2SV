# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_occ={}
        t_occ={}
        for i,v in enumerate(s):
            if v in s_occ:
                s_occ[v].append(i)
            else:
                s_occ[v]=[i]
        for i,v in enumerate(t):
            if v in t_occ:
                t_occ[v].append(i)
            else:
                t_occ[v]=[i]
        tt=t_occ.values()
        ss=s_occ.values()
        tt.sort()
        ss.sort()
        
        return tt==ss
            
            

        