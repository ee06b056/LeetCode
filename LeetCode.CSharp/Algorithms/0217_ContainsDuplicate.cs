using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0217_ContainsDuplicate
{
    public bool ContainsDuplicate(int[] nums)
    {
        var numberSet = new HashSet<int>();
        foreach (int n in nums)
        {
            if (!numberSet.Add(n)) return true;
        }
        return false;
    }
}
