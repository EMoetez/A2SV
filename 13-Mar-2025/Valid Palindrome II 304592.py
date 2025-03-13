# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub_s: str) -> bool:
            return sub_s == sub_s[::-1]

        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s[l+1:r+1]) or is_palindrome(s[l:r])
            l += 1
            r -= 1
            
        return True  
