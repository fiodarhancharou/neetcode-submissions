class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        i = 0
        size = len(s)
        is_reachable = [False]*size
        is_reachable[0] = True
        # s = [00110010]
        for i in range(1, size):
            # i = 1, s[i] = 0
            if s[i] == "0":
                for j in range(minJump, maxJump+1):
                    if is_reachable[i-j]:
                        is_reachable[i] = True
                        break
        return is_reachable[-1]