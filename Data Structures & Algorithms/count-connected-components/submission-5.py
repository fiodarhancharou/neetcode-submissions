from collections import defaultdict, deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        indegree = [0]*n
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            graph[a].add(b)
            graph[b].add(a)
        visited = set()
        count = 0
        for node in range(n):
            if not node in visited:
                count += 1
                q = deque([node])
                while q:
                    nxt = q.popleft()
                    visited.add(nxt)
                    for neib in graph[nxt]:
                        if neib in visited:
                            continue
                        q.append(neib)
        return count
        