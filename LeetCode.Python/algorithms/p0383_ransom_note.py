from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_c = Counter(ransomNote)
        m_c = Counter(magazine)
        for char, count in r_c.items():
            if m_c[char] < count:
                return False
        return True