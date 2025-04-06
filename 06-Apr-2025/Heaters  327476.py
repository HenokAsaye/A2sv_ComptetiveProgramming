# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0
        right = 1 * 10**9
        ans = 0
        def validate(n):
            for house in houses:
                index = bisect_left(heaters,house)
                left_heater = heaters[index-1] if index >0  else float("-inf")
                right_heater = heaters[index] if index < len(heaters) else float("inf")
                if(min(abs(house-left_heater),abs(house-right_heater))  > n):
                    return False
            return True
        while left <= right:
            mid = (left + right) //2
            if(validate(mid)):
                ans = mid
                right = mid-1
            else:
                left =  mid+1
        return ans
        