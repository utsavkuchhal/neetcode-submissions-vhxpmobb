class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        max_time = 0
        while q:
            row, col, time = q.popleft()
            for r, c in directions:
                nr, nc = row + r, col + c
                if nr >= n or nc >= m or nr < 0 or nc < 0:
                    continue
                if grid[nr][nc] == 1:
                    q.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
                    max_time = max(max_time, time + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max_time
        