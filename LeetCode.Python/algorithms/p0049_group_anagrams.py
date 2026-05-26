from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupdict = defaultdict(list)
        for s in strs:
            groupdict[tuple(sorted(s))].append(s)
        return list(groupdict.values())
