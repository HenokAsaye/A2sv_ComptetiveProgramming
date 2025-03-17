# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(n,m):
            if not n and not m:
                return True
            if not n or not m:
                return False
            if n.val != m.val:
                return False
            s1 = helper(n.left,m.right)
            s2 = helper(n.right,m.left)
            return s1 and s2
        return helper(root,root)





                    

        
        