class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        buckets = [0]*3
        for num in nums:
            buckets[num] += 1
        res = []
        j = 0
        for i, bucket in enumerate(buckets):
            while bucket:
                nums[j] = i
                bucket -= 1
                j += 1