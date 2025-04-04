# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)  
        ans = []
        for num in nums:
            count[num] += 1  
        for i in range(1, n + 1):
            if count[i] == 2:
                ans.append(i)  
        for i in range(1, n + 1):
            if(count[i]==0):
                ans.append(i)
        return ans
