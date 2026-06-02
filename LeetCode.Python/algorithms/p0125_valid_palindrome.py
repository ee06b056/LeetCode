class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(c for c in s if c.isalnum()).lower()
        i = 0
        j = len(new_s) - 1
        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def isPalindromeOptimized(self, s: str) -> bool:
        new_s = "".join(c for c in s if c.isalnum()).lower()
        return new_s == new_s[::-1]
