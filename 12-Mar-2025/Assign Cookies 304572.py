# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        happy=0
        n,m=0,0
        while n < len(g) and m < len(s):
            if g[n]<=s[m]:
                happy+=1
                n+=1
                m+=1
            else:
                m+=1
            if m==len(s) or n==len(g):
                break
        return happy