from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        n_conn = [0]*n
        graph = defaultdict(list)
        for a, b in edges:
            n_conn[a] += 1
            n_conn[b] += 1
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque(i for (i,n) in enumerate(n_conn) if n == 1)
        while q:
            node = q.popleft()
            for con in graph[node]:
                n_conn[con] -= 1
                if n_conn[con] == 1:
                    q.append(con)
        for i in n_conn:
            if i != 0:
                return False  
        return True