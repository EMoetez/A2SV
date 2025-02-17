# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0

        distinct=set(nums)
        longest_seq=0

        for element in distinct:
            if element-1 not in distinct:
                curr_seq=1
                last_value=element
                while last_value+1 in distinct:
                    curr_seq+=1
                    last_value+=1
                longest_seq=max(longest_seq,curr_seq)
        return longest_seq
