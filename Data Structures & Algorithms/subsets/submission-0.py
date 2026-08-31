import copy


class Solution:
    def backtrack(self, index, curr_arr):
        curr_arr = copy.copy(curr_arr)
        self.result.append(curr_arr)
        for i in range(index,len(self.nums)):
            curr_arr.append(self.nums[i])
            self.backtrack(i+1, curr_arr)
            curr_arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.nums = nums
        self.backtrack(0, [])
        return self.result

