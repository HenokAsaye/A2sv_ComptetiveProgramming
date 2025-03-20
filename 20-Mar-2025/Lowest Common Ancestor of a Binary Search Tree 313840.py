# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def helper(root,p,q):
            nonlocal ans
            if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
                ans = root
                return root
            if(root.val > p.val and root.val >q.val):
                return helper(root.left,p,q)
            if(root.val < p.val and root.val < q.val):
                return helper(root.right,p,q)
        helper(root,p,q)
        return ans
    

        