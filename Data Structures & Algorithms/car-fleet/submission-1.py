class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        items_sorted = sorted(zip(position, speed))
        times = [(target-p)/s for p,s in items_sorted]
        stack = []
        for t in times[::-1]:
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)
            


