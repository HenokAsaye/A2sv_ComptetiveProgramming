# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        flag = False
        minimum = float("-inf")  
        
        for i in reversed(nums):  
            if i < minimum:  
                return True
            while stack and stack[-1] < i:
                minimum = stack.pop()
            stack.append(i)
        
        return False
