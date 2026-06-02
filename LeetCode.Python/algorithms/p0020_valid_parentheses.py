class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case "{" | "[" | "(":
                    stack.append(char)
                case "}":
                    if not stack or stack[-1] != "{":
                        return False
                    stack.pop()
                case "]":
                    if not stack or stack[-1] != "[":
                        return False
                    stack.pop()
                case ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
        return not stack
