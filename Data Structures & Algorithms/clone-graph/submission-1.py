"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from copy import deepcopy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        graph_map = {}
        graph_map[node] = Node(node.val)
        queue = deque([node])
        while queue:
            current_node = queue.popleft()
            for neighbour in current_node.neighbors:
                if neighbour not in graph_map:
                    graph_map[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                graph_map[current_node].neighbors.append(graph_map[neighbour])
        return graph_map[node]
            
                
