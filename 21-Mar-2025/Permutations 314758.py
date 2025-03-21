# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        def backTrack(start):
            if len(path) == len(nums):
                if (len(path) == len(set(path))):
                    ans.append(path.copy())
                return
            for candidate in nums:
                path.append(candidate)
                backTrack(candidate)
                path.pop()

        backTrack(0)
        return ans
        