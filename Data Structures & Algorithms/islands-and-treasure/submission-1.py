class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        wave_source = deque()

        n_row, n_col = len(grid), len(grid[0])
        inf = 2147483647

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    wave_source.append((i,j))

        while wave_source:
            r, c = wave_source.popleft()
            for i, j in ((r-1, c), (r+1,c), (r,c-1), (r,c+1)):
                if i >= 0 and j >= 0 and i < n_row and j < n_col and grid[i][j] == inf:
                    grid[i][j] = grid[r][c] + 1
                    wave_source.append((i,j))




                

        