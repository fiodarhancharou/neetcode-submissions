class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 1
        res1, res2 = True, True
        while l <= r:
            if s[l] != s[r]:
                if count:
                    l += 1
                    count -= 1
                    continue
                else:
                    res1 = False
                    break
            l += 1
            r -= 1
        count = 1
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                if count:
                    r -= 1
                    count -= 1
                    continue
                else:
                    res2 = False
                    break
            l += 1
            r -= 1
        if res1 or res2:
            return True
        else:
            return False
