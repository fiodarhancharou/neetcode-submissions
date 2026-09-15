class Solution:
    def rob(self, nums: List[int]) -> int:
        # split the problem in two: without the first number
        # and without the last number, return the maximum of them
        n = len(nums)
        if n <= 3:
            return max(nums)
        store = [0]*n
        def dfs(i):
            if i>=n:
                return 0
            elif store[i] != 0:
                return store[i]
            res = max(nums[i]+dfs(i+2), dfs(i+1))
            store[i] = res
            return res
        first_res = dfs(1)
        n -= 1
        store = [0]*n
        second_res = dfs(0)
        return max(first_res, second_res)