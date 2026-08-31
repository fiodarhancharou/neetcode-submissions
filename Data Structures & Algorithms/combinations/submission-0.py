class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(index, arr):
            if len(arr) == k:
                result.append(arr[:])
            for i in range(index,n+1):
                arr.append(i)
                if len(arr) <= k:
                    backtrack(i+1, arr)
                arr.pop()
        backtrack(1, [])
        return result