class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        counter = set()
        max_size = 0
        while r < len(s):
            if s[r] not in counter:
                counter.add(s[r])
                r += 1
                max_size = max(max_size, r-l)
            else:
                while s[r] in counter:
                    counter.remove(s[l])
                    l += 1
        return max_size

