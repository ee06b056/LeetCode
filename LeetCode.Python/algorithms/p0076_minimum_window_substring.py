from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = Counter(t)
        require = len(need)
        s_counter = defaultdict(int)
        have = 0
        best_left, best_len = 0, float('inf')
        left = 0
        for i, c in enumerate(s):
            s_counter[c] += 1
            if c in need and need[c] == s_counter[c]:
                have += 1
            while have == require:
                if i - left + 1 < best_len:
                    best_left, best_len = left, i - left + 1
                lc = s[left]
                s_counter[lc] -= 1
                if lc in need and s_counter[lc] < need[lc]:
                    have -= 1
                left += 1
        return "" if best_len == float('inf') else s[best_left: best_left + best_len]