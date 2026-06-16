class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeObj = {
            '}': '{',
            ')': '(',
            "]": '['
        }
        for c in s:
            if c in closeObj:
                if stack and stack[-1] == closeObj[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        