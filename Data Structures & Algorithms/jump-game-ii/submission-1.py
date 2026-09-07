class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        jumps = 0
        cur_level = [0]
        target = len(nums) - 1
        while cur_level:
            jumps += 1
            next_level = set()
            for cur_pos in cur_level:
                for next_pos in range(cur_pos+1, min(cur_pos+nums[cur_pos]+1, len(nums))):
                    if next_pos == target:
                        return jumps
                    next_level.add(next_pos)
            cur_level = next_level
        return jumps

                