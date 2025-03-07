# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        max_time=0
        for i in range(0,len(tasks),4):
            process_time=processorTime[i//4]+tasks[i]
            max_time=max(max_time,process_time)
        return max_time

