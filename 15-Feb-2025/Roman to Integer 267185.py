# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map={'I':1,'V':5,"X":10,'L':50,'C':100,'D':500,'M':1000}
        num=hash_map[s[-1]]
        if len(s)==1:
            
            return num
        for i in range(len(s)-2,-1,-1):
            print(hash_map[s[i]],hash_map[s[i+1]])
            if hash_map[s[i]] >= hash_map[s[i+1]]:
                num+=hash_map[s[i]]
            else:
                num-=hash_map[s[i]]
        return num
