from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list) # node -> list(neib)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        print(adj)
        def dfs(node):
            visited[node] = True
            for neib in adj[node]:
                if not visited[neib]:
                    dfs(neib)

        visited = [False]*n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count

        