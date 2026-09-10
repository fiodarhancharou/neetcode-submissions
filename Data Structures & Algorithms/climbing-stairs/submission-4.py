class Solution:
    def climbStairs(self, n: int) -> int:
        prev_res = [1,2]
        if n <= 2:
            return prev_res[n-1]
        for i in range(2,n):
            print(prev_res)
            prev_res.append(prev_res[i-1] + prev_res[i-2])
        return prev_res[-1]