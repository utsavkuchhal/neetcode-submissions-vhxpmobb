# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root == None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        curr_diam = self.height(root.left) + self.height(root.right)
        return max(curr_diam, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))