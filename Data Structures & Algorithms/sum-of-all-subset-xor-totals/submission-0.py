class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = 0
        def backtrack(start, path):
            XOR = 0
            for i, num in enumerate(path):
                if i == 0:
                    XOR = num
                else:
                    XOR ^= num

            self.result += XOR
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return self.result