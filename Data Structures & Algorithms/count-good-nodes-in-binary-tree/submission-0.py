# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        def dfs(root, curr_max):
            if not root:
                return
            if root.val >= curr_max:
                result.append(root.val)
            if root.val > curr_max:
                curr_max = root.val
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)
        dfs(root, float('-inf'))
        return len(result)

