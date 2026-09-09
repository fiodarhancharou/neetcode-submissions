from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        i = 0
        # nums=[1,2,1,0,4,2,6]
        # k=3
        while i < len(nums):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i >= k-1:
                result.append(nums[window[0]])
            i += 1
            if window[0] == i - k:
                window.popleft()
        return result