class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 1:
            return nums
        for i in range(1,size):
            j = i
            while j>0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums
