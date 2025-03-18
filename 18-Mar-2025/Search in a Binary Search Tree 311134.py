# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None
        def helper(root):
            nonlocal ans
            if root:
                if(root.val > val):
                    helper(root.left)
                elif(root.val < val):
                    helper(root.right)
                else:
                    ans = root
        helper(root)
        return ans
                


    
                
        
        