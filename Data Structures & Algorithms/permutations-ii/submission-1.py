class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(index, arr, seen):
            if len(arr) == len(nums):
                res.add(tuple(arr))
                return
            
            for i in range(0, len(nums)):
                if i not in seen:
                    arr.append(nums[i])
                    seen.append(i)
                    backtrack(index, arr, seen)
                    arr.pop()
                    seen.pop()
        backtrack(0, [], [])
        return [list(i) for i in res]