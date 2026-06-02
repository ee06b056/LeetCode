from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        sc = Counter(s)
        length = 0
        hasOdd = False
        for v in sc.values():
            if v % 2 == 1:
                hasOdd = True
                length += v - 1
            else:
                length += v
        if hasOdd:
            length += 1
        return length