# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = sum(candies)
        ans = 0
        def checker(c_s):
            s = 0
            for num in candies:
                s += num // c_s
            return s>=k
        while left <= right:
            mid = (left + right) //2
            if(checker(mid)):
                ans = mid
                left = mid + 1
            else:
                right = mid -1
        return ans
        