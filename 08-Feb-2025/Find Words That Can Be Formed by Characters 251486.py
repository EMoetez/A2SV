# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res=0
        count= Counter(chars)

        for word in words:
            tmp_c=Counter(word)
            good=True

            for char in word:
                
                if char not in count or  tmp_c[char]> count[char]:
                    good=False
                    break
            if good:
                res+=len(word)
        return res
            

     
