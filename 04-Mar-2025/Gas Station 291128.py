# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)  
        total_cost = sum(cost)  
        if total_gas < total_cost:  
            return -1  
        x = 0  
        start = 0  
        for i in range(len(gas)):
            x += gas[i] - cost[i]  
            if x < 0:  
                x = 0  
                start = i + 1  
        return start  
