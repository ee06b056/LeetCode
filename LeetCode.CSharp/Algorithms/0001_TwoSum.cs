using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

class _0001_TwoSum
{
    public int[] TwoSum(int[] nums, int target) {

        var set = new HashSet<int>();
        foreach (var i in nums)
        {
            var compNum = target - i;
            if (set.Contains(compNum))
            {
                return new int[] {i, compNum};
            }
            set.Add(i);
        }
        
        return Array.Empty<int>();
    }
}
