class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(board, row, col, visited, index, word):
            if index == len(word) - 1:
                return True
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            has_word = False
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == word[index + 1] and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    has_word |= solve(board, row + x, col + y, visited, index + 1, word)
                    visited[new_row][new_col] = False
            return has_word

        row_len = len(board)
        col_len = len(board[0])
        visited = [[False] * col_len for _ in range(row_len)]
        for row in range(row_len):
            for col in range(col_len):
                if word[0] == board[row][col]:
                    visited[row][col] = True
                    solution = solve(board, row, col, visited, 0, word)
                    visited[row][col] = False
                    if solution:
                        return True
        return False