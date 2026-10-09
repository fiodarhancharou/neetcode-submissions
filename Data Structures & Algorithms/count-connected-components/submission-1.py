from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)] # node -> list(neib)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False]*n
        def dfs(node):
            visited[node] = True
            for neib in adj[node]:
                if not visited[neib]:
                    dfs(neib)
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count

        