class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            a, b = heapq.heappop(neg_stones), heapq.heappop(neg_stones)
            diff = -abs(a-b)
            if diff != 0:
                heapq.heappush(neg_stones, diff)
        return -neg_stones[-1] if len(neg_stones) == 1 else 0