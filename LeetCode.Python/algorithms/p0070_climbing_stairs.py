class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        pre1 = 1
        pre2 = 1
        for i in range(2, n + 1):
            pre2, pre1 = pre2 + pre1, pre2
        return pre2
    
    def climbStairs_optimized(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b