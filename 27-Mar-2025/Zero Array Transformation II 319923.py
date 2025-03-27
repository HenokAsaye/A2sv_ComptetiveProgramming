# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if(sum(nums)==0):
            return 0
        right = len(queries) -  1
        left = 0
        ans = -1
        def checker(k):
            arr = [0] * (len(nums)+1)
            for i in range(k+1):
                arr[queries[i][0]] += queries[i][2]
                arr[(queries[i][1])+1] -= queries[i][2]
            for j in range(1,len(arr)):
                arr[j] = arr[j] + arr[j-1]
            for r in range(len(nums)):
                if(nums[r] > arr[r]):
                    return False
            return True
        while left <= right:
            mid = (left + right) // 2
            if(checker(mid)):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        if(ans == -1):
            return -1
        else:
            return ans + 1
        