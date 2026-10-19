class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        res = 0
        for l in n:
            if l == "1":
                res += 1
        return res