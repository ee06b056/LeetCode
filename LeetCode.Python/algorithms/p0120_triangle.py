class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        dp = [0] * m
        for i in range(m):
            for j in range(i, -1, -1):
                if i == 0 and j == 0:
                    dp[j] = triangle[i][j]
                elif j == 0:
                    dp[j] += triangle[i][j]
                elif j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
        return min(dp)

    def minimumTotal_bottom_up(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]