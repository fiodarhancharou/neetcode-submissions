class Solution:
    from collections import deque
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(heights), len(heights[0])


        def bfs(cells):
            visited = set(cells)
            queue = deque(cells)
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if (0<=dr<n_rows and 0<=dc<n_cols and (dr, dc) not in visited and heights[dr][dc] >= heights[r][c]):
                        visited.add((dr, dc))
                        queue.append((dr, dc))
            return visited
        
        pacific_init = [(0, c) for c in range(n_cols)] + [(r, 0) for r in range(n_rows)]
        atlantic_init = [(n_rows-1, c) for c in range(n_cols)] + [(r, n_cols-1) for r in range(n_rows)]

        pacific_cells = bfs(pacific_init)
        atlantic_cells = bfs(atlantic_init)

        return [[item[0], item[1]] for item in pacific_cells & atlantic_cells]
