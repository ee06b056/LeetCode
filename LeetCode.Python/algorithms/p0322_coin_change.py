class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {0: 0}
        def fewest(amount: int) -> int:
            if amount < 0:
                return float("inf")
            if amount in dp:
                return dp[amount]
            else:
                count = min(fewest(amount - coin) for coin in coins)
                dp[amount] = 1 + count
                return 1 + count
        answer = fewest(amount)
        return answer if answer != float("inf") else -1
    
    def coinChange_bottom_up(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                pre = i - c
                if pre >= 0:
                    dp[i] = min(dp[i], dp[pre] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1