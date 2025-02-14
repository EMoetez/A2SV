# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res=[]
        count=Counter(nums)
        target=len(nums)//3

        for i, freq in count.items():
            if freq > target:
                res.append(i)
        return res

        