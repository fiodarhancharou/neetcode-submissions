class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [0]*n
        for i in range(n):
            if i < 2:
                res[i] = cost[i]
            else:
                res[i] = min((res[i-1]+cost[i]),(res[i-2]+cost[i]))
        print(res)
        return min(res[-1],res[-2])