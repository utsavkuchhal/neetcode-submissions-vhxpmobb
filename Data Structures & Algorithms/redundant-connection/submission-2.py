class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        print(self.parent)

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return True
        else:
            self.parent[parent_v] = parent_u
            return False

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u, v in edges:
            if uf.union(u, v):
                return [u, v]
        