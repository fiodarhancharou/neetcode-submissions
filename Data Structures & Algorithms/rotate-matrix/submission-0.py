import copy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res = copy.deepcopy(matrix)
        # convert i-th row to -i-th col
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                # 0, 0 -> 0, 2
                # 0, 1 -> 1, 2
                # 0, 2 -> 2, 2

                # 1, 0 -> 0, 1
                # 1, 1 -> 1, 1
                # 1, 2 -> 2, 1

                # 2, 0 -> 0, 0
                # 2, 1 -> 1, 0
                # 2, 2 -> 2, 0

                res[c][cols-1-r] = matrix[r][c]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = res[i][j]