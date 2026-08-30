import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [0] * 26
        for task in tasks:
            heap[ord(task)-ord('A')] -= 1
        heap = [i for i in heap if i<0]
        heapq.heapify(heap)
        time = 0
        while heap:
            storage = []
            for i in range(n+1):
                if heap:
                    item = heapq.heappop(heap)
                    if item < -1:
                        item += 1
                        storage.append(item)
                    time += 1
                elif storage:
                    time += 1
            while storage:
                heapq.heappush(heap, storage.pop())
        return time
        
