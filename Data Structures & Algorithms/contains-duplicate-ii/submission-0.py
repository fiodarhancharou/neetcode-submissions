from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        counter = {}
        l, r = 0, 0
        while r < size:
            if counter and counter.get(nums[r]):
                return True
            counter[nums[r]] = counter.get(nums[r], 0) + 1
            if r >= k:
                counter[nums[l]] -= 1
                l += 1
            r += 1
        return False
