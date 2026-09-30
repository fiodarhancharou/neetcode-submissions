class Solution:

    def is_pos(self, a):
        if a > 0:
            return True
        elif a < 0:
            return False
        
    def same_sign(self, a, b):
        if (self.is_pos(a) and self.is_pos(b)) or (not self.is_pos(a) and not self.is_pos(b)):
            return True
        return False

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or self.same_sign(a, stack[-1]):
                stack.append(a)
                continue
            a_is_destroyed = False
            while stack and (stack[-1] > 0 and a < 0):                
                if abs(stack[-1]) > abs(a):
                    a_is_destroyed = True
                    break
                elif abs(stack[-1]) == abs(a):
                    a_is_destroyed = True
                    stack.pop()
                    break
                else:
                    stack.pop()
            if not a_is_destroyed:
                stack.append(a)
        return stack