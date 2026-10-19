class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        rows, cols = len(matrix), len(matrix[0])
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        r, c = 0, 0
        next_r, next_c = r, c
        res = []
        dirs_i = 0
        while True:  
            res.append(matrix[r][c])
            visited.add((r,c))
            if len(visited) == rows*cols:
                return res
            next_r += dirs[dirs_i][0]
            next_c += dirs[dirs_i][1]
            while not 0 <= next_r < rows or not 0 <= next_c < cols or (next_r, next_c) in visited:
                next_r, next_c = r, c
                if dirs_i >= 3:
                    dirs_i = 0
                else:
                    dirs_i += 1
                next_r += dirs[dirs_i][0]
                next_c += dirs[dirs_i][1]
            r, c = next_r, next_c
        return res