from collections import defaultdict, deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)] # node -> list(neib)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False]*n
        count = 0
        q = deque()
        for i in range(n):
            if not visited[i]:
                count += 1
                q.append(i)
                while q:
                    node = q.popleft()
                    visited[node] = True
                    for neib in adj[node]:
                        if not visited[neib]:
                            q.append(neib)
        return count

        