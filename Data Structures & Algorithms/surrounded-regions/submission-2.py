class Solution:
    def dfs(self, i, j, board):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return
        if board[i][j] == "X" or board[i][j] == "#":
            return

        board[i][j] = "#"
        for r, c in directions:
            self.dfs(i + r, j + c, board)


    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        for i in range(0, n):
            if board[i][0] == "O":
                self.dfs(i, 0, board)
            if board[i][m - 1] == "O":
                self.dfs(i, m - 1, board)
    
        for i in range(0, m):
            if board[0][i] == "O":
                self.dfs(0, i, board)
            if board[n - 1][i] == "O":
                self.dfs(n - 1, i, board)

        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] ==  "#":
                    board[i][j] = "O"
                    
        