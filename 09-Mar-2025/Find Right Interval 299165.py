# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        h_map={}
        sts=[]
        ends=[]
        output=[]
        for index, interval in enumerate(intervals):
            sts.append([interval[0],index])
            ends.append(interval[1])

        ends.sort()
        sts=sorted(sts, key=lambda x: x[0])
        i,j=0,0
        while i<len(ends) and j<len(sts) :
            if ends[i]<=sts[j][0]:
                h_map[ends[i]]=sts[j][1]
                i+=1
            else:
                j+=1
        for st,e in intervals:
            result=h_map.get(e,-1)
            output.append(result)
        return output



