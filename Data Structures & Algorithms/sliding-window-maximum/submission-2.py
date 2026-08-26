from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # implementation using heap
        l, r = 0, 0
        window = deque()
        while r < k:
            if not window or nums[window[-1]] > nums[r]:
                window.append(r)
            else:
                while window and nums[window[-1]] <= nums[r]:
                    window.pop()
                window.append(r)
            r += 1
        res = [nums[window[0]]]
        while r < len(nums):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            while window and window[0] < r - k + 1:
                window.popleft()
            window.append(r)
            if len(window) > k:
                window.popleft()
            res.append(nums[window[0]])
            l += 1
            r += 1
        return res