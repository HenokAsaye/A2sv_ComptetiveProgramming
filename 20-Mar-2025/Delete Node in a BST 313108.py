# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(root):
            current = root
            while current.left:
                current = current.left
            return current
        def helper(root,key):
            if not root:
                return root
            if key < root.val:
                root.left = helper(root.left,key)
            elif key > root.val:
                root.right = helper(root.right,key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                temp = minValueNode(root.right)
                root.val = temp.val
                root.right = helper(root.right,temp.val)
            return root
        return helper(root,key)
                    
            