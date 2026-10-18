from collections import deque
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))
        heap = []
        heapq.heappush(heap, [0, k])
        visited = set()
        t = 0
        while heap:
            w, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = w
            for neib, w_neib in adj[node]:
                if neib in visited:
                    continue
                heapq.heappush(heap, (t+w_neib, neib))

        return t if len(visited) == n else -1
        
            