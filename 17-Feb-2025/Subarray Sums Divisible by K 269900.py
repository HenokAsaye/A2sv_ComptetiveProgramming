# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        prefix_sum =0
        count =0
        for i in nums:
            prefix_sum +=i
            remainder = prefix_sum%k
            if(remainder in prefix_sum_count):
                count += prefix_sum_count[remainder]
            prefix_sum_count[remainder] +=1
        return count