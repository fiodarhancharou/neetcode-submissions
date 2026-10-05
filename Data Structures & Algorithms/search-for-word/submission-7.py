class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])
        res = False
        def backtrack(board_pos, word_pos, seen):
            nonlocal res
            for direction in dirs:
                next_pos = board_pos[0] + direction[0], board_pos[1] + direction[1]
                if word_pos < len(word) and (
                    next_pos[0] >= 0 and next_pos[0] < rows
                ) and (
                    next_pos[1] >= 0 and next_pos[1] < cols
                ) and (
                    next_pos not in seen
                ):
                    if board[next_pos[0]][next_pos[1]] == word[word_pos]:
                        if word_pos == (len(word) - 1):
                            res = True
                            return
                        seen.add(next_pos)
                        backtrack(next_pos, word_pos+1, seen)
                        seen.remove(next_pos)
                else:
                    continue

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if len(word) == 1:
                        return True
                    backtrack((r,c), 1, {(r,c)})
        return res