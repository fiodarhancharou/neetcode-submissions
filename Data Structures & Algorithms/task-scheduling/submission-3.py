import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = {}
        for task in tasks:
            heap[task] = heap.get(task, 0) + 1
        heap = [[-n, task] for task, n in heap.items()]
        heapq.heapify(heap)

        count = 0
        while heap:
            stack = []
            for _ in range(n+1):
                if heap:
                    cur_task = heapq.heappop(heap)
                    cur_task[0] += 1
                    if cur_task[0] != 0:
                        stack.append(cur_task)
                    count += 1
                elif stack:
                    count += 1
            while stack:
                heapq.heappush(heap, stack.pop())
        return count
                
