class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def backtrack(arr, seen):
            if len(arr) == len(nums):
                res.add(tuple(arr))
                return
            
            for i in range(0, len(nums)):
                if i not in seen:
                    arr.append(nums[i])
                    seen.append(i)
                    backtrack(arr, seen)
                    arr.pop()
                    seen.pop()
        backtrack([], [])
        return [list(i) for i in res]