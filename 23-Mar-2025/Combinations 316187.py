# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def backTrack(start):
            if len(path) == k:
                ans.append(path.copy())
                return
            for candidate in range(start+1,n+1):
                path.append(candidate)
                backTrack(candidate)
                path.pop()
        backTrack(0)
        return ans
            


        




        