class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0]*size*2
        for i, num in enumerate(nums):
            res[i] = num
            res[i+size] = num 
        return res