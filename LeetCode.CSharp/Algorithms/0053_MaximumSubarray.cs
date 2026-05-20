using System;

namespace LeetCode.CSharp.Algorithms;

public class _0053_MaximumSubarray
{
    public int MaxSubArray(int[] nums)
    {
        int maxSum = int.MinValue;
        int sum = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            sum += nums[i];
            maxSum = Math.Max(sum, maxSum);
            if (sum < 0)
            {
                sum = 0;
            }
        }
        return maxSum;
    }
}
