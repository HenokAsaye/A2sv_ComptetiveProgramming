# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m_d = 0
        def helper(root,depth):
            nonlocal m_d
            if not root:
                m_d = max(m_d,depth)
                return m_d
            helper(root.left,depth+1)
            helper(root.right,depth+1)
        helper(root,0)
        return m_d
        
            

        