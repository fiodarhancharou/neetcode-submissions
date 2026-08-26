class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        longest = s[0]

        res = []
        for i in range(len(s)):
            # Odd palindromes
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            # Even palindromes
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
        return longest