# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l=len(arr)
        maxim=l
        output=[]
        while maxim>1:
            idx=arr.index(maxim)
            if idx!=maxim-1:
                if idx!=0:
                    arr[:idx+1]=arr[:idx+1][::-1]
                    output.append(idx+1)
                
                arr[:maxim]=arr[:maxim][::-1]
                output.append(maxim)
            maxim-=1  
        return output

