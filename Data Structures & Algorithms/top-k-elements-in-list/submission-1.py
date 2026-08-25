class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key in counter:
            buckets[counter[key]].append(key)
        res = []
        index = -1
        while len(res) < k:
            res.extend(buckets[index])
            index -= 1
        return res
