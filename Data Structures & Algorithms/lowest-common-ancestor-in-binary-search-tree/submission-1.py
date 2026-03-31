# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val, q_val = p.val, q.val
        while root:
            if p_val <= root.val <= q_val or q_val <= root.val <= p_val:
                return root
            elif p_val < root.val:
                root = root.left
            else:
                root = root.right
        return root
