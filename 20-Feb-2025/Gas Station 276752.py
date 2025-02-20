# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0
        current_tank = 0
        start_index = 0  
        for i in range(len(gas)):
            balance = gas[i] - cost[i]
            total_tank += balance  
            current_tank += balance  
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0  
        return start_index if total_tank >= 0 else -1