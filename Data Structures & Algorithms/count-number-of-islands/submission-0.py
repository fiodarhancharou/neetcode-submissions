class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((0,1), (1,0), (-1,0), (0,-1))
        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(r+dr,c+dc)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                count += 1
                dfs(r, c)
        return count