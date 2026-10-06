from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm
        n_prereqs = [0]*numCourses
        node_parents = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            node_parents[b].append(a)
            n_prereqs[a] += 1
        
        q = deque(i for i, n in enumerate(n_prereqs) if n == 0)
        count = 0
        while q:
            course = q.popleft()
            count += 1
            for parent in node_parents[course]:
                n_prereqs[parent] -= 1
                if n_prereqs[parent] == 0:
                    q.append(parent)
        return count == numCourses
