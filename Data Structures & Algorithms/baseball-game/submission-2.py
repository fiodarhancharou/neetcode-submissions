class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = set(("+", "C", "D"))
        for o in operations:
            if not o in ops:
                stack.append(int(o))
                continue
            if o == "+":
                stack.append(stack[-1]+stack[-2])
            elif o == "C":
                stack.pop()
            elif o == "D":
                stack.append(stack[-1]*2)
        return sum(stack)