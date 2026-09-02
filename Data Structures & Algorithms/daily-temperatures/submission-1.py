class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # [0, 0, 0]
        i = 0
        stack = []
        while i < len(temperatures): # i < 3
            while stack and temperatures[i] > temperatures[stack[-1]]:
                day = stack.pop()
                result[day] = i - day # [2, 1, 0]
            stack.append(i) # stack = [22, 21]
            i += 1 # i = 1
        return result