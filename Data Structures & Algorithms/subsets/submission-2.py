import copy


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)
        def backtrack(cur_i, arr):
            arr = copy.copy(arr)
            res.append(arr)
            if cur_i == size:
                return
            for i in range(cur_i, size):
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()
        backtrack(0, [])
        return res