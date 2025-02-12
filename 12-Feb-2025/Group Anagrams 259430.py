# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams={}
        for i in strs:
            key = tuple(sorted(i))
            if key in anagrams:
                anagrams[key].append(i)
            else:
                anagrams[key]=[i]
        
        return [v for k,v in anagrams.items()]
