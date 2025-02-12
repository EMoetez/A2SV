# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairs=0
        num_left=0
        count=Counter(nums)
        print(count)
        for k,v in count.items():
            pairs+= v//2
            if v %2==1:
                num_left+=1
        return [pairs, num_left]
            

