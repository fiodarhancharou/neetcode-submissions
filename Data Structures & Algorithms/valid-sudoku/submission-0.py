class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        # check rows
        for i in range(rows):
            chars = set(str(i) for i in range(1,10))
            for j in range(cols):
                char = board[i][j]
                if not char == ".":
                    if char in chars:
                        chars.remove(char)
                    else:
                        return False
        # check cols
        for i in range(cols):
            chars = set(str(i) for i in range(1,10))
            for j in range(rows):
                char = board[j][i]
                if not char == ".":
                    if char in chars:
                        chars.remove(char)
                    else:
                        return False
        # check subsquares
        for i in range(3):
            for j in range(3):
                chars = set(str(i) for i in range(1,10))
                for r in range(i*3, i*3+3):
                    for c in range(j*3, j*3+3):
                        char = board[r][c]
                        if not char == ".":
                            if char in chars:
                                chars.remove(char)
                            else:
                                return False
        return True