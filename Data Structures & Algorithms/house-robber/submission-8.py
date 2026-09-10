class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        res = []
        if size >= 1:
            res.append(nums[0])
            if size == 1:
                return res[-1]
        if size >= 2:
            res.append(max(nums[0], nums[1]))
            if size == 2:
                return res[-1]
        if size >= 3:
            res.append(max([nums[0]+nums[2], nums[1]]))
            if size == 3:
                return res[-1]
        for i in range(3, size):
            res.append(max([res[-2], res[-3]])+nums[i])
        return max([res[-1], res[-2]])
