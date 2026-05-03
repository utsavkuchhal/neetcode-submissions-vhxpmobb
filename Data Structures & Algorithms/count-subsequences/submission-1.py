class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        
        def dfs(s, t, i, j, dp):
            if j == len(t):
                return 1
            
            if i >= len(s):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            total = 0
            if s[i] == t[j]:
                total += dfs(s, t, i + 1, j + 1, dp)
            total += dfs(s, t, i + 1, j, dp)

            dp[i][j] = total
            return total
        
        dp = [[-1] * len(t) for _ in range(len(s))]
        return dfs(s, t, 0, 0, dp)