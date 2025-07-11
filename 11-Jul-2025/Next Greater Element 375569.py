# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack=[]
        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()
            next_greater[i]=stack[-1] if stack else -1
            stack.append(i)
        return [next_greater[i] for i in nums1]





    
        
        
        