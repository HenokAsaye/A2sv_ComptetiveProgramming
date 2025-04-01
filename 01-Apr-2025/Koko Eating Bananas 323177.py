# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        ans = 1
        def validate(n):
            time = 0
            for i in piles:
                time +=ceil(i/n)
            if time > h:
                return False
            return True
        while left <= right:
            mid = (left+right)//2
            if validate(mid):
                ans = mid
                right = mid -1 
            else:
                left = mid +1
        return ans
                


