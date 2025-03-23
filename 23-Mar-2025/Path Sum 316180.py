# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = []
        def helper(root,path):
            nonlocal ans
            if not root:
                return 
            path.append(root.val)
            if not root.left and not root.right:
                ans.append(path[:])
            helper(root.left,path)
            helper(root.right,path)
            path.pop()
        helper(root,[])
        for i in range(len(ans)):
            if (sum(ans[i]) == targetSum):
                return True
        return False




        