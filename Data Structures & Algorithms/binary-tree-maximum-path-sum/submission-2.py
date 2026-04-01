# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def solve(root):
            if not root:
                return 0
            
            l_max_sum = max(0, solve(root.left))
            r_max_sum = max(0, solve(root.right))
            self.ans = max(self.ans, l_max_sum + r_max_sum + root.val)

            return root.val + max(l_max_sum, r_max_sum)
        solve(root)
        return self.ans



        