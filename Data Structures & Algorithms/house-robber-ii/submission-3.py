class Solution:
    def rob(self, nums: List[int]) -> int:
        # split the problem in two: without the first number
        # and without the last number, return the maximum of them

        size = len(nums)
        if size <=3:
            return max(nums)
        def rob_1(start, end):
            res = [0,0,0]
            for i in range(start, end):
                res.append(max([res[-2], res[-3]])+nums[i])
            return max([res[-1], res[-2]])
        return max(rob_1(1,size), rob_1(0,size-1))