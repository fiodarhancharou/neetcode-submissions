class Solution:
    def rob(self, nums: List[int]) -> int:
        # split the problem in two: without the first number
        # and without the last number, return the maximum of them

        size = len(nums)
        if size <=3:
            return max(nums)
        res = [0,0,0]
        for i in range(1,size):
            res.append(max([res[-2], res[-3]])+nums[i])
        first_res = max([res[-1], res[-2]])
        size -= 1
        res = [0,0,0]
        for i in range(size):
            res.append(max([res[-2], res[-3]])+nums[i])
        second_res = max([res[-1], res[-2]])
        return max(first_res, second_res)