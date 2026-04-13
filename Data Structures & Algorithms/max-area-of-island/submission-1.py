class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            area = 0
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            while q:
                row, col = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(max_area, area)

        return max_area