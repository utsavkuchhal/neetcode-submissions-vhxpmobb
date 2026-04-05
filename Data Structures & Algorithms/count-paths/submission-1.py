class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(0, n + 1)]
        for row in range(n):
            dp[row][0] = 1
        for col in range(m):
            dp[0][col] = 1
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[n - 1][m - 1]