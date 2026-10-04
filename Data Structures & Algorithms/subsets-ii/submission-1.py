class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, cur_arr):
            res.append(tuple(sorted(cur_arr[:])))
            for i in range(index, len(nums)):
                cur_arr.append(nums[i])
                backtrack(i+1, cur_arr)
                cur_arr.pop()
        
        backtrack(0, [])
        res = [list(i) for i in set(res)]
        return res