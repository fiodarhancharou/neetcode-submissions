class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k last become k first
        # len(nums) - k first become last

        # [1,2,3,4,5,6,7,8], k = 3
        # [6,7,8,1,2,3,4,5]
        k = k % len(nums)
        for _ in range(k):
            # make one rotation
            l, r = len(nums)-2, len(nums)-1 
            while l >= 0:
                nums[l], nums[r] = nums[r], nums[l]
                l -= 1
                r -= 1
            