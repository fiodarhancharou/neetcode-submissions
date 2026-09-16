class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        for i in range(size):
            while nums[i] == val:
                nums[i], nums[size-1] = nums[size-1], '!'
                size -= 1
        return size