# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        
        target_numbers = set(range(left, right + 1))
        
        
        for start, end in ranges:
            for num in range(start, end + 1):
                if num in target_numbers:
                    target_numbers.remove(num)
        
        
        return len(target_numbers) == 0

