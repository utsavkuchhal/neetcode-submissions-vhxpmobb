# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        return self.buildBTree(preorder, inorder, 0, len(preorder) - 1)

    def search(self, val, arr, left, right):
        for index in range(left, right + 1):
            if arr[index] == val:
                return index
        return -1

    def buildBTree(self, preorder, inorder, left, right):
        if left > right:
            return None
        
        root = TreeNode(preorder[self.pre_index])
        in_index = self.search(preorder[self.pre_index], inorder, left, right)
        self.pre_index += 1
        root.left = self.buildBTree(preorder, inorder, left, in_index - 1)
        root.right = self.buildBTree(preorder, inorder, in_index + 1, right)
        return root
