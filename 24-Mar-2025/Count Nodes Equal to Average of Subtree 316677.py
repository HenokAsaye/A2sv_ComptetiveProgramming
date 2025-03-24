# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if not root:
                return (0,0)
            left_sum,left_count = helper(root.left)
            right_sum, right_count = helper(root.right)
            total_sum = right_sum + left_sum + root.val
            total_count = right_count + left_count + 1
            avg = total_sum // total_count
            if avg == root.val:
                count +=1
            return(total_sum,total_count)
        helper(root)
        return count

            


        