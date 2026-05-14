using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0015_3Sum
{
    public IList<IList<int>> ThreeSum(int[] nums)
    {
        List<IList<int>> answer = [];
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 2; i++)
        {
            if (i != 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1, k = nums.Length - 1;
            while (j < k)
            {
                if (nums[j] + nums[k] == - nums[i])
                {
                    answer.Add([nums[i], nums[j], nums[k]]);
                    j++;
                    k--;
                    while (j < k && nums[j - 1] == nums[j]) j++;
                    while (j < k && nums[k + 1] == nums[k]) k--; 
                } else if (nums[j] + nums[k] < - nums[i])
                {
                    j++;
                } else
                {
                    k--;
                }
            }
        }
        return answer;
    }
}