class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c >=cols or grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0
            visited[r][c] = True
            return dfs(r, c+1) + dfs(r+1, c) + dfs(r,c-1) + dfs(r-1,c)
                
        visited = [[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)
        
        return 0