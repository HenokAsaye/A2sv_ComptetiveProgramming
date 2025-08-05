# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root):
            val =root.val
            queue = deque([root])
            ans = []
            print(queue)
            print(len(queue))
            while queue:
                current = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    current.append(node.val)

                    if(node.left):
                        queue.append(node.left)
                    if(node.right):
                        queue.append(node.right)
                ans.append(current)
            return ans

        return []
       

            
            