class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict: dict[str, int] = {}
        max_l = 0
        current_i = -1
        for i, c in enumerate(s):
            if c in char_dict:
                current_i = max(current_i, char_dict[c])
            char_dict[c] = i
            max_l = max(max_l, i - current_i)
        return max_l