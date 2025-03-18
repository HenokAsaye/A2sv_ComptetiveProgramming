# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(c_max,root,c_min):
            if not root:
                return c_max - c_min

            c_max = max(c_max,root.val)
            c_min = min(c_min,root.val)
            left =  helper(c_max,root.left,c_min)
            right = helper(c_max,root.right,c_min)
            return max(left,right)

        return helper(float("-inf"),root,float("inf"))
        
        
        
        
            
            