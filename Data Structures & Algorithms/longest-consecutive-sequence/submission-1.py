from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        distinct_nums = list(nums_set)
        res = 0
        for num in distinct_nums:
            cur_res = 0
            pref = num - 1
            if pref in nums_set:
                continue
            else:
                post = num
                while post in nums_set:
                    cur_res += 1
                    post += 1
                res = max(res, cur_res)
        return res