from collections import defaultdict, deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                print(parent[x], x)
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        count = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                count -= 1

        return count

        