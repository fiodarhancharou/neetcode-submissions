class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0]*size*2
        for i in range(size):
            res[i] = nums[i]
            res[i+size] = nums[i]
        return res