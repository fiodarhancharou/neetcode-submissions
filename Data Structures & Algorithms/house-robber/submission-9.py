class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size <=2:
            return max(nums)
        res = [nums[0], max(nums[0], nums[1]), max([nums[0]+nums[2], nums[1]])]
        for i in range(3, size):
            res.append(max([res[-2], res[-3]])+nums[i])
        return max([res[-1], res[-2]])
