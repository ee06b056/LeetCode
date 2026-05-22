using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0973_KClosestPointsToOrigin
{
    public int[][] KClosest(int[][] points, int k) 
    {
        var pq = new PriorityQueue<(int, int), int>(Comparer<int>.Create((x, y) => y.CompareTo(x)));
        foreach (int[] point in points)
        {   int x = point[0], y = point[1];
            if (pq.Count < k)
            {
                pq.Enqueue((x, y), x * x + y * y);
            }
            else
            {
                pq.EnqueueDequeue((x, y), x * x + y * y);
            }
        }
        var kPoints = new int[k][];
        for (int i = 0; i < k; i++)
        {
            var (x, y) = pq.Dequeue();
            kPoints[i] = [x, y];
        }
        return kPoints;
    }
}
