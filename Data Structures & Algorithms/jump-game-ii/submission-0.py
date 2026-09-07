class Solution:
    def jump(self, nums: List[int]) -> int:
        n_jumps = 0
        i = 0
        max_next_pos = 0
        cur_end = 0
        for i in range(len(nums)-1):
            max_next_pos = max(max_next_pos, i + nums[i])
            if i == cur_end:
                cur_end = max_next_pos
                n_jumps += 1
                if cur_end >= len(nums) - 1:
                    break
        return n_jumps
                