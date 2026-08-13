class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = 1
                elif j == 0:
                    dp[j] = 1
                else:
                    dp[j] = dp[j - 1] + dp[j]
        return dp[-1]

    