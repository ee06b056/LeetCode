class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def to_list(s: str) -> list[str]:
            lst = []
            for c in s:
                if c == "#":
                    if len(lst) > 0:
                        lst.pop()
                else:
                    lst.append(c)
            return lst
        sl, tl = to_list(s), to_list(t)
        return sl == tl

    def backspaceCompare_constant_space(self, s: str, t: str) -> bool:
        def next_valid(s: str, i: int) -> int:
            skip_count = 0
            while i >= 0:
                if s[i] == "#":
                    skip_count += 1
                elif skip_count > 0:
                    skip_count -= 1
                else:
                    return i
                i -= 1
            return -1
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = next_valid(s, i)
            j = next_valid(t, j)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True