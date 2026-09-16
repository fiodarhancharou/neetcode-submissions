class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = 0
        i = 0
        continu = True
        for i, cur_l in enumerate(strs[0]):

            for string in strs:
                if i > len(string)-1 or string[i] != cur_l:
                    continu = False
                    break
            if not continu:
                break
            res += 1
        return strs[0][:res]