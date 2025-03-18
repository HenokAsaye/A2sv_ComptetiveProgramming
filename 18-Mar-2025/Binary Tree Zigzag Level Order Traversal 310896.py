# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def helper(node, depth):
            if not node:
                return
            if (len(ans) == depth):
                ans.append([])
            if(depth %2 == 0):
                ans[depth].append(node.val)
            else:
                ans[depth].insert(0,node.val)
            helper(node.left,depth+1)
            helper(node.right,depth+1)
        helper(root,0)
        return ans

