# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        left_st = self.invertTree(root.left)
        right_st = self.invertTree(root.right)
        root.left = right_st
        root.right = left_st
        return root