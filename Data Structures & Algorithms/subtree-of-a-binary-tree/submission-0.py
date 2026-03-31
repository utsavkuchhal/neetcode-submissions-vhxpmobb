# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        queue = [(p, q)]
        while queue:
            n1, n2 = queue.pop()
            if not n1 and not n2:
                continue
            
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            node = queue.pop()
            if self.isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
