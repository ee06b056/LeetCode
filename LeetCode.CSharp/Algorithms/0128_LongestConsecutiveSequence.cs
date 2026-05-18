using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0128_LongestConsecutiveSequence
{
    public int LongestConsecutive(int[] nums)
    {
        if (nums.Length == 0) return 0;
        int longestLength = 1;
        HashSet<int> numSet = new();
        foreach (int n in nums)
        {
            numSet.Add(n);
        }
        foreach(int n in numSet)
        {
            if (!numSet.Contains(n - 1))
            {
                int l = 0;
                int tempN = n;
                while (numSet.Contains(tempN))
                {
                    l++;
                    tempN++;
                }
                longestLength = Math.Max(longestLength, l);
            }
        }
        return longestLength;
    }
}
