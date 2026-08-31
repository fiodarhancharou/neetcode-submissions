class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(arr, used_nums):

            if len(arr) == len(nums):
                result.append(arr[:])
                return

            for i in range(len(nums)):
                if nums[i] not in used_nums:
                    arr.append(nums[i])
                    used_nums.add(nums[i])
                    backtrack(arr, used_nums)
                    used_nums.remove(nums[i])
                    arr.pop()

        backtrack([], set())

        return result