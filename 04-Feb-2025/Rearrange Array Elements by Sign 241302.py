# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pos=[]
        neg=[]
        output=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        
        for i in range(len(pos)):

            output.append(pos[i])
            output.append(neg[i])
        
        return output

                


