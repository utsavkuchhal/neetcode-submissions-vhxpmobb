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
            #max can be the path from this root
            self.ans = max(self.ans, l_max_sum + r_max_sum + root.val)
            # while returning we return root_val + max(l, r) as prarent can take only path left or right
            return root.val + max(l_max_sum, r_max_sum)
        solve(root)
        return self.ans



        