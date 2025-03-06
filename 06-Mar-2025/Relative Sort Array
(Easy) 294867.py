# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        common={}
        not_common=[]
        result=[]
        for i in arr1:
            if i in arr2:
                common[i]=common.get(i,0)+1
            else:
                not_common.append(i)
        not_common.sort()
        for i in arr2:
            for _ in range(common[i]):
                result.append(i)
        return result+not_common

        