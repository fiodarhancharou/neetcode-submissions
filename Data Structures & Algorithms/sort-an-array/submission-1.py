class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size < 2:
            return nums
        mid = size // 2
        left = [num for num in nums if num < nums[mid]]
        middle = [num for num in nums if num == nums[mid]]
        right = [num for num in nums if num > nums[mid]]
        return self.sortArray(left) + middle + self.sortArray(right)
