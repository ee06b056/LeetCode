using System;

namespace LeetCode.CSharp.Algorithms;

public class _0121_BestTimeToBuyAndSellStock
{
    public int MaxProfit(int[] prices)
    {
        int profit = 0;
        int minPrice = int.MaxValue;
        foreach (int price in prices)
        {
            profit = Math.Max(profit, price - minPrice);
            minPrice = Math.Min(minPrice, price);
        }
        return profit;
    }
}
