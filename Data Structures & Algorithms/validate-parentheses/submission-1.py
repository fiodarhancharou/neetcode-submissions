class Solution:
    def isValid(self, s: str) -> bool:
        br_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for br in s:
            if br in br_map:
                if not stack or br_map[br] != stack.pop():
                    return False
            else:
                stack.append(br)
        is_empty = not bool(stack)
        return is_empty