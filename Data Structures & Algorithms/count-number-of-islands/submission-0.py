class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        else:
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # method 1 -> use dfs to mark connected 
        # components visited and count how many times called DFs 

        #method 2 -> we can use bfs  + visited array
        # same complexity m * n and space m * n

        #method 3 -> Disjoint set, we will use this still same complexity
        #but we need to revise this
        directions = [
            (-1, 0), (0, -1),
            (1, 0), (0, 1)
        ]
        n, m = len(grid), len(grid[0])
        uf = UnionFind(n * m)

        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    for r, c in directions:
                        nrow, ncol = row + r, col + c
                        if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == "1":
                            uf.union(row * m + col, nrow * m + ncol)

        uniqueIslands = set()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    uniqueIslands.add(uf.find(r * m + c))

        return len(uniqueIslands)
                    



