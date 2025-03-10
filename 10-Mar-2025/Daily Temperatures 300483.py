# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result=[0]*len(temperatures)
        stack=[]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_indx = stack.pop()
                result[stack_indx] = i-stack_indx
            stack.append([temperatures[i],i])
        return result
                