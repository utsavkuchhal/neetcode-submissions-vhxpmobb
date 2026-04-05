# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        output = ""
        while queue:
            node = queue.popleft()
            output += str(node.val) + "," if node else "N,"
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return output[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        if not arr or arr[0] == 'N':
            return None

        root = TreeNode(int(arr[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()

            # Left child
            if arr[i] != 'N':
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(arr) and arr[i] != 'N':
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1

        return root
