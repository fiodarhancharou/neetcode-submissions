class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for num in nums[:-1]:
            left.append(left[-1]*num)
        pref = 1
        for i in range(1,len(nums)+1):
            left[-i] = left[-i]*pref
            pref = pref * nums[-i]
        return left

            