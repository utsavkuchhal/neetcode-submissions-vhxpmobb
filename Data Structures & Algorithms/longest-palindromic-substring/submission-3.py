class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        rs = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        max_len, last_index = 0, 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rs[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if i - dp[i][j] == n - j:
                        if max_len < dp[i][j]:
                            max_len = max(max_len, dp[i][j])
                            last_index = i
                else:
                    dp[i][j] = 0
        return s[last_index - max_len: last_index]

                