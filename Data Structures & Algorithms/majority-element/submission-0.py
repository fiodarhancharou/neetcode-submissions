class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        size = len(nums)
        mid = size // 2
        return nums[mid]
            
