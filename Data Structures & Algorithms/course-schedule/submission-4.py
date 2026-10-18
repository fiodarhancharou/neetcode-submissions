from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [set() for _ in range(numCourses)]
        indegree = [0]*numCourses # n prereqs for each course
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].add(a)

        q = deque(i for i, c in enumerate(indegree) if c == 0)
        count = 0
        while q:
            course = q.popleft()
            count += 1
            for parent in adj[course]:
                indegree[parent] -= 1
                if indegree[parent] == 0:
                    q.append(parent)
        return count == numCourses