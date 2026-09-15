class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size <=2:
            return max(nums)
        res = [0,0,0]
        for i in range(size):
            res.append(max([res[-2], res[-3]])+nums[i])
        print(res)
        return max([res[-1], res[-2]])
