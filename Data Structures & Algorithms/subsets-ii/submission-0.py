class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, cur_arr):
            res.append(cur_arr[:])
            for i in range(index, len(nums)):
                cur_arr.append(nums[i])
                backtrack(i+1, cur_arr)
                cur_arr.pop()
        
        backtrack(0, [])
        res = (tuple(sorted(i)) for i in res)
        res = list(set(res))
        res = [list(i) for i in res]
        return res