# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(n,m,depth):
            if not n or not m:
                return 
            if (depth % 2 != 0):
                n.val,m.val = m.val,n.val
            helper(n.left,m.right,depth+1)
            helper(n.right,m.left,depth+1)
        helper(root.left,root.right,1)
        return root
        
                
