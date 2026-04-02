class UninonFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False
        else:
            self.parent[parent_v] = parent_u
            return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UninonFind(n)
        for u, v in edges:
            uf.union(u, v)
        parent_set = set()
        for i in range(n):
            parent_set.add(uf.find(i))

        return len(parent_set)