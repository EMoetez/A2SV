# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        tmp=0
        for j in nums:
                if j % 2==0:
                    tmp+=j
        print("the default sum",tmp)
               
        for modif in queries:
            
            
            if (nums[modif[1]]%2==0) and (modif[0]%2==0):
                print("1")
                tmp+=modif[0]
                res.append(tmp)
                 
            elif ((nums[modif[1]]%2)!=0) and ((modif[0]%2)!=0):
                print("2")
                tmp+=(modif[0]+nums[modif[1]])
                res.append(tmp)

            elif ((nums[modif[1]]%2)==0) and ((modif[0]%2)!=0):
                print("3")
                tmp-=nums[modif[1]]
                res.append(tmp)
            else:
                print("4")
                res.append(tmp)
            nums[modif[1]]+=modif[0]
            tmp=res[-1] 
        return res