class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        res = ""
        size1, size2 = len(word1), len(word2)
        for i in range(min(size1, size2)):
            res += word1[i]
            res += word2[i]
        if size1 == size2:
            return res
        elif size1 < size2:
            res += word2[i+1:]
        else:
            res += word1[i+1:]
        return res