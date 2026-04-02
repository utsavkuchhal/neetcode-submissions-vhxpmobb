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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UninonFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        parent_set = set()
        for i in range(n):
            parent_set.add(uf.find(i))

        return True if len(parent_set) == 1 else False