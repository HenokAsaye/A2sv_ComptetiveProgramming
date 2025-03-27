# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = max(ranks) * cars * cars
        ans = 0
        def checker(p_min):
            res = 0
            for num in ranks:
                res += (floor(sqrt(p_min // num)))
            return res >= cars
        while left <= right:
            mid = (left + right) // 2
            if(checker(mid)):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans

