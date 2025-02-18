# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = []
        for i in nums:
            if(i%2==0):
                ans.append(0)
            else:
                ans.append(1)   
        counter = defaultdict(int)
        counter[0] =1
        count =0
        prefix_sum = 0
        for j in ans:
            prefix_sum +=j
            print(prefix_sum)
            if(prefix_sum-k) in counter:
                count +=counter[prefix_sum-k]
            counter[prefix_sum]+=1
        return count

