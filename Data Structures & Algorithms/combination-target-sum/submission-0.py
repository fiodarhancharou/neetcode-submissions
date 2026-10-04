class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, arr):
            arr = arr[:]
            s = sum(arr)
            if arr and s == target:
                res.append(arr[:])
            elif s > target:
                return
            for i in range(index,len(nums)):
                arr.append(nums[i])
                backtrack(i, arr)
                arr.pop()

        backtrack(0, [])
        return res