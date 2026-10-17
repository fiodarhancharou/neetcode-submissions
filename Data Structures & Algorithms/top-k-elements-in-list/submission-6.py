import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for key in counter:
            bucket[counter[key]].append(key)
        res = []
        for b in bucket[::-1]:
            while b:
                res.append(b.pop())
                k -= 1
                if k == 0:
                    return res
        return res
