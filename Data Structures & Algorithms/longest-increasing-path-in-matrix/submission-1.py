class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def solve(matrix, row, col, dp):
            if dp[row][col] != -1:
                return dp[row][col]

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            max_val = 0
            for r, c in directions:
                nr, nc = row + r, col + c
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and (
                    matrix[nr][nc] > matrix[row][col]
                ):
                    max_val = max(max_val, solve(matrix, nr, nc, dp) + 1)
            dp[row][col] = max_val
            return max_val
        
        result = 0
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, solve(matrix, i, j, dp) + 1)
        return result