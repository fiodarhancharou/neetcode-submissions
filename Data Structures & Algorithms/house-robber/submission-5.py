class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        store = [0]*n
        def dfs(i):
            if i>=n:
                return 0
            elif store[i] != 0:
                return store[i]
            res = max(nums[i]+dfs(i+2), dfs(i+1))
            store[i] = res
            return res
        
        return dfs(0)
