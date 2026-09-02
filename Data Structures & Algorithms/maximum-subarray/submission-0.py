class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_sum = float("-inf")
        cur_sum = 0
        while r < len(nums):
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                l = r
                cur_sum = 0
            r+=1
        return max_sum