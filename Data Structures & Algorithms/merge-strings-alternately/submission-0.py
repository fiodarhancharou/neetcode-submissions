class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        res = []
        size1, size2 = len(word1), len(word2)
        min_word = "1" if size1 <= size2 else "2"
        for i in range(min(size1, size2)):
            res.append(word1[i])
            res.append(word2[i])
        res = "".join(res)
        if size1 == size2:
            return res
        elif size1 < size2:
            res += word2[i+1:]
        else:
            res += word1[i+1:]
        return res