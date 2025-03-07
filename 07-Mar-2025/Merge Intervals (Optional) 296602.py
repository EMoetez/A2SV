# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        st, end = intervals[0]
        output=[]
        if len(intervals)==1:
            return intervals

        for s, e in intervals[1:]:
            if  s<=end : 
                end=max(end,e)
            else:
                output.append([st,end])
                st,end=s,e
        output.append([st,end])
        return output
            
                
            
