# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        summation = 0
        i=0
        j=len(piles)-1
        while i < j:
            summation +=piles[j-1]
            i+=1
            j-=2
        return summation




