from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(i, j, visited):
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            q = deque()
            q.append((i, j, 0))
            while q:
                row, col, dist = q.popleft()
                visited[row][col] = True
                for r, c in directions:
                    nr, nc = row + r, col + c
                    if nr >= n or nc >= m or nr < 0 or nc < 0 or grid[nr][nc] in [0, -1] or visited[nr][nc]:
                        continue
                    q.append((nr, nc, dist + 1))
                    grid[nr][nc] = min(grid[nr][nc], dist + 1)

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visited = [[False] * m for _ in range(n)]
                    bfs(i, j, visited)
    