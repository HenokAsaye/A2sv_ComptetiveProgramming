# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count =0
        x=coins
        i=0
        if(coins < costs[0]):
            return 0
        while i < len(costs):
            if(x >= costs[i]):
                x-=costs[i]
                count +=1
            i+=1
        return count







        