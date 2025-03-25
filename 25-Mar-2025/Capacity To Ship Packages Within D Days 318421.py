# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = []
        while left <= right:
            mid = (left + right) // 2  
            summation = 0
            i = 0
            count_days = 1
            while i < len(weights):
                if summation + weights[i] > mid:  
                    count_days += 1
                    summation = 0
                summation += weights[i]
                i += 1
            if count_days > days:  
                left = mid + 1
            else:  
                ans.append(mid)
                right = mid - 1
        return min(ans)







'''
55

10

mid = 10 + 55 = 65 // 2 = 32



55 - 32 = 23



'''



        