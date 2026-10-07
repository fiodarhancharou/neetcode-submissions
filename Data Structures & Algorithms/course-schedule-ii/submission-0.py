from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # a -> b -> c
        n_prereqs = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            n_prereqs[a] += 1
            graph[b].append(a)
        
        q = deque(i for i, n in enumerate(n_prereqs) if n == 0)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for parent in graph[course]:
                n_prereqs[parent] -= 1
                if n_prereqs[parent] == 0:
                    q.append(parent)
        for i in n_prereqs:
            if i != 0:
                return []
        return res