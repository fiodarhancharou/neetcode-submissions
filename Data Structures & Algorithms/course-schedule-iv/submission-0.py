class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # a -> b -> c
        n_prereqs = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            n_prereqs[b] += 1
            graph[a].append(b)
        
        q = deque(i for i, n in enumerate(n_prereqs) if n == 0)
        prereqs = [set() for _ in range(numCourses)]
        while q:
            course = q.popleft()
            for parent in graph[course]:
                prereqs[parent].add(course)
                prereqs[parent] = prereqs[parent].union(prereqs[course])
                n_prereqs[parent] -= 1
                if n_prereqs[parent] == 0:
                    q.append(parent)
        res = []
        for i, j in queries:
            res.append(i in prereqs[j])
        return res