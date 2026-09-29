class Solution:

    # 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7

    # 1, 2, 3, 4, 3, 5, 5, 6, 7
    # 1, 2, 3, 4, 5, 3, 5, 6, 7
    # 1, 2, 3, 4, 5, 6, 5, 3, 7
    # 1, 2, 3, 4, 5, 6, 7, 3, 5
 
    def removeDuplicates(self, nums: List[int]) -> int:
        # indeces of the first and last elements for the window with repeated chars
        l, r = 0, 1 # empty window
        size = len(nums)
        while r < size:
            # compare the element left to the window and with index r
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
            r += 1
        return l+1