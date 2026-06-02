import math

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = math.inf
        max_profit = 0
        for p in prices:
            lowest = min(lowest, p)
            max_profit = max(max_profit, p - lowest)
        return max_profit