# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        word_sets = [set(word) for word in words]
        max_prod = 0

        for i in range(n):
            for j in range(i + 1, n):  
                if not (word_sets[i] & word_sets[j]):  
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))

        return max_prod
