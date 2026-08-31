import copy


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = nums

        def backtrack(index, curr_arr):
            result.append(curr_arr[:])
            for i in range(index,len(nums)):
                curr_arr.append(nums[i])
                backtrack(i+1, curr_arr)
                curr_arr.pop()
        backtrack(0, [])
        return result

