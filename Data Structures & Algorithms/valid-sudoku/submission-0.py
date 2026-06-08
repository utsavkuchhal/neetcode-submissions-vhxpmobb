class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        if n != m:
            return False
        for i in range(n):
            horizontal_set = set()
            for j in range(n):
                val = board[j][i]
                if val in horizontal_set:
                    return False
                if val != '.':
                    horizontal_set.add(val)
            print(horizontal_set)
        
            vertical_set = set()
            for j in range(n):
                val = board[i][j]
                if val in vertical_set:
                    return False
                if val != '.':
                    vertical_set.add(val)
            print(vertical_set)
            if i % 3 == 0:
                for j in range(n):
                    if j % 3 == 0:
                        new_set = set()
                        for k in range(i, i + 3):
                            for l in range(j, j + 3):
                                val = board[k][l]
                                if val in new_set:
                                    return False
                                if val != '.':
                                    new_set.add(val)
                        print(new_set)
        return True

