class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0
        while l < r:
            cur_vol = (r - l) * min(heights[l],heights[r])
            max_vol = max(max_vol, cur_vol)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                l += 1
        return max_vol