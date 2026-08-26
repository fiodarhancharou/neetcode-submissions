class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            # Odd palindromes
            l, r = i, i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    res.append(s[l:r+1])
                    l -= 1
                    r += 1
                else:
                    break
            # Even palindromes
            l, r = i, i+1
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    res.append(s[l:r+1])
                    l -= 1
                    r += 1
                else:
                    break

        return max([(len(i), i) for i in res])[1]