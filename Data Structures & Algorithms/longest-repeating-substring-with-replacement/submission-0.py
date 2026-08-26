class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_w = 0
        counter = {}
        max_f = 0
        max_size = 0
        while r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1
            max_f = max(max_f, counter[s[r]])
            r += 1
  
            while not max_f + k >= r - l:
                counter[s[l]] -= 1
                l += 1
            max_size = max(max_size, r - l)
        return max_size