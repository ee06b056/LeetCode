from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_arr = [int(v) for v in version1.split(".")]
        v2_arr = [int(v) for v in version2.split(".")]
        for v1, v2 in zip_longest(v1_arr, v2_arr, fillvalue=0):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0