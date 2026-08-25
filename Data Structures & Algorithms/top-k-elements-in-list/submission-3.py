import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        res = []
        for key, val in counter.items():
            heapq.heappush(res, (val, key))
            if len(res) > k:
                heapq.heappop(res)
        return [i[1] for i in res]

