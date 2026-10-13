class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        size = len(nums)
        cur_sum = 0
        max_sum = float("-inf")
        while r < size:
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
            if cur_sum <= 0:
                cur_sum = 0
            r += 1
        return max_sum