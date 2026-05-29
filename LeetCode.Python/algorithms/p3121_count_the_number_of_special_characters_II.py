class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_dict = {}
        for c in word:
            lower_c = c.lower()
            if c.islower():
                if c not in char_dict:
                    char_dict[lower_c] = 0
                if char_dict[lower_c] == 1:
                    char_dict[lower_c] = -1
            if c.isupper():
                if lower_c not in char_dict:
                    char_dict[lower_c] = -1
                if char_dict[lower_c] == 0:
                    char_dict[lower_c] = 1
        return sum(1 for v in char_dict.values() if v == 1)

    def numberOfSpecialCharsShort(self, word: str) -> int:
        first_upper = {}
        last_lower = {}
        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                first_upper.setdefault(c.lower(), i)
        return sum(1 for c, i in last_lower.items() if c in first_upper and i < first_upper[c])