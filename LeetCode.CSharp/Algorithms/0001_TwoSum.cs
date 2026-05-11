using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0001_TwoSum
{
    public int[] TwoSum(int[] nums, int target) 
    {
        var dict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            var value = nums[i];
            var complement = target - value;
            if (dict.TryGetValue(complement, out var index))
            {
                return [index, i];
            }
            dict.TryAdd(value, i);
        }
        
        throw new InvalidOperationException("No two sum solution");
    }
}
