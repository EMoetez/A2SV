# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #This is my submission
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        print(len(nums)/2)
        print(dic)
        for i in dic:
            if dic[i]>(len(nums)//2):
                return i
        
        # # Trying Boyer moore algorithm
        # res, count=0,0
        # for n in nums:
        #     if count==0:
        #         res=n
        #     if res == n:
        #         count+=1
        #     else:
        #         count-=1
        # return res
            
         