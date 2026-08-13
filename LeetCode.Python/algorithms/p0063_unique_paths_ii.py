class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif i == 0 and j == 0:
                    dp[j] = 1
                elif i == 0:
                    dp[j] = dp[j - 1] + dp[j]
                elif j == 0:
                    pass
                else:
                    dp[j] = dp[j - 1] + dp[j]
        return dp[n - 1]