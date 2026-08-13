class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for i in range(1, n):
            ndp = [0] * n
            for j in range(n):
                lu = dp[j - 1] if j > 0 else float("inf")
                mu = dp[j]
                ru = dp[j + 1] if j < n - 1 else float("inf")
                ndp[j] = min(lu, mu, ru) + matrix[i][j]
            dp = ndp
        return min(dp)