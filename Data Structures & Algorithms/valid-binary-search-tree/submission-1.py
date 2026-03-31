# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            traversal.append(root.val)
            root = root.right

        for index in range(1, len(traversal)):
            if traversal[index] <= traversal[index - 1]:
                return False
        return True

