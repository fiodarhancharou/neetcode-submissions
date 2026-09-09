from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        i = 0
        size = len(s)
        is_reachable = [False]*size
        is_reachable[0] = True

        window = deque() # the number of points from which we can reach the current one
        while i < size:
            if i - minJump >= 0 and s[i-minJump] == "0" and is_reachable[i-minJump]:
                window.append(i-minJump)
            if s[i] == "0":
                if window:
                    is_reachable[i] = True
            i += 1
            if window and i - maxJump >= 0 and window[0] == i - maxJump - 1:
                window.popleft()
        return is_reachable[-1]