# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, current_number):
            nonlocal ans
            if not node:
                return
            current_number = current_number * 10 + node.val
            if not node.left and not node.right:
                ans += current_number
                return
            dfs(node.left, current_number)
            dfs(node.right, current_number)
        dfs(root, 0)
        return ans
