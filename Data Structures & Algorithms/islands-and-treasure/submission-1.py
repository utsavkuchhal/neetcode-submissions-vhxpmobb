from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            for r, c in directions:
                nr, nc = row + r, col + c
                if nr >= n or nc >= m or nr < 0 or nc < 0:
                    continue
                if grid[nr][nc] == 2147483647:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[row][col] + 1


    