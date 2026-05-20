using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0057_InsertInterval
{
    public int[][] Insert(int[][] intervals, int[] newInterval) 
    {
        List<int[]> answerIntervals = new();
        foreach (int[] interval in intervals)
        {
            if (interval[1] < newInterval[0])
            {
                answerIntervals.Add(interval);
            } 
            else if ( newInterval[1] < interval[0] )
            {
                answerIntervals.Add(newInterval);
                newInterval = interval;
            }
            else
            {
                int left = Math.Min(interval[0], newInterval[0]);
                int right = Math.Max(interval[1], newInterval[1]);
                newInterval = [left, right];
            }
        }
        answerIntervals.Add(newInterval);
        return answerIntervals.ToArray();
    }
}
