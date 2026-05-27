from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chardict = defaultdict(set)
        count = 0
        for char in word:
            chardict[char.lower()].add(char)
        for vset in chardict.values():
            if len(vset) == 2:
                count += 1
        return count