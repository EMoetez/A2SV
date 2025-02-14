# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        exist=[]
        
        for start, end in ranges:
            for i in range(left,right+1):
                if i <= end and i>= start:
                    exist.append(i)
        return len(set(exist))==right-left +1
        

