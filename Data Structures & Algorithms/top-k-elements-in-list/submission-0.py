class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        print(help(sorted))
        sorted_counter = sorted(list(counter.items()), key = lambda x: x[1], reverse=True)
        return [i[0] for i in sorted_counter[:k]]