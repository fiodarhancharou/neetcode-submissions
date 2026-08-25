class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 11:27
        stack = []
        res = [0]*len(temperatures)
        for i, cur_t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_t:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        return res

            