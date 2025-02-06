# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        summ=0
        for j in nums:
                if j % 2==0:
                    summ+=j
        
               
        for modif in queries:
            
            
            if (nums[modif[1]]%2==0) and (modif[0]%2==0):
                
                summ+=modif[0]
                res.append(summ)
                 
            elif ((nums[modif[1]]%2)!=0) and ((modif[0]%2)!=0):
                
                summ+=(modif[0]+nums[modif[1]])
                res.append(summ)

            elif ((nums[modif[1]]%2)==0) and ((modif[0]%2)!=0):
                
                summ-=nums[modif[1]]
                res.append(summ)
            else:
                
                res.append(summ)
            nums[modif[1]]+=modif[0]
            summ=res[-1] 
        return res