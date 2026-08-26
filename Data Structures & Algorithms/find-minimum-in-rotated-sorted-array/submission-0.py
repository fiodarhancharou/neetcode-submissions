class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        glob_min = float('inf')
        while l <= r:
            mid = (l+r)//2
            if nums[l] <= nums[mid]:
                sorted_min = nums[l]
                l = mid + 1
            else:
                sorted_min = nums[mid]
                r = mid - 1
            glob_min = min(glob_min, sorted_min)
        return glob_min
