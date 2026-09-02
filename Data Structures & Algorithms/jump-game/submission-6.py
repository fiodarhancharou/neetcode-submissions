class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        end = size - 1
        i = end - 1
        while end > 0 and i > 0: # [2,5,0,0]
            print(end, i, nums[i])
            if not nums[i] >= end - i:
                i -= 1
            else:
                end = i
                i = end - 1
                
        if end==0 or nums[i] >= end - i:
            return True
        return False
                