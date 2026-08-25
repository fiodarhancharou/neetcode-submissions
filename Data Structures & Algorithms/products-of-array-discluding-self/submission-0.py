class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for num in nums[:-1]:
            left.append(left[-1]*num)
        left
        right = [1]
        for num in nums[::-1][:-1]:
            right.append(right[-1]*num)
        
        right = right[::-1]
        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res