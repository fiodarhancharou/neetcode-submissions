import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        counter_tuples = [(item[1], item[0]) for item in counter.items()]
        res = []
        for item in counter_tuples:
            heapq.heappush(res, item)
            if len(res) > k:
                heapq.heappop(res)
        return [i[1] for i in res]

