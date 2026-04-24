# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, curr_max):
            if not root:
                return 0

            count = 0
            if root.val >= curr_max:
                count += 1
            if root.val > curr_max:
                curr_max = root.val
            count += dfs(root.left, curr_max)
            count += dfs(root.right, curr_max)
            return count
        return dfs(root, float('-inf'))

