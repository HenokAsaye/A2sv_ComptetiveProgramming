# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        prev = [-1] * n
        next = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next[i] = stack[-1]
            stack.append(i)
        result = 0
        for i in range(n):
            result += arr[i] * (i - prev[i]) * (next[i] - i)
            result %= MOD
        return result
