# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dic = defaultdict(lambda : float("-inf"))
        def helper(n,depth):
            if not n:
                return
            dic[depth] = max(dic[depth],n.val)
            helper(n.left,depth+1)
            helper(n.right,depth+1)
        helper(root,0)
        return [dic[d] for d in sorted(dic.keys())]



