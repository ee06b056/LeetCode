from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        for char in s:
            match char:
                case "{" | "[" | "(":
                    dq.append(char)
                case "}":
                    if not dq or dq[-1] != "{":
                        return False
                    dq.pop()
                case "]":
                    if not dq or dq[-1] != "[":
                        return False
                    dq.pop()
                case ")":
                    if not dq or dq[-1] != "(":
                        return False
                    dq.pop()
        return len(dq) == 0
