# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        def helper(root):
            if root:
                helper(root.left)
                ans.append(root.val)
                helper(root.right)
        helper(root)
        def build(ans):
            if not ans:
                return 
            mid = len(ans)//2
            root = TreeNode(ans[mid])
            root.left = build(ans[:mid])
            root.right = build(ans[mid+1:])
            return root
        return build(ans)
