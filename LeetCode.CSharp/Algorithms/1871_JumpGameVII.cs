using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _1871_JumpGameVII
{
    public bool CanReach(string s, int minJump, int maxJump)
    {
        if (s[s.Length - 1] == '1') return false;
        var visited = new int[s.Length];
        visited[0] = 1;
        var queue = new Queue<int>();
        queue.Enqueue(0);
        while (queue.Count > 0)
        {
            var index = queue.Dequeue();
            for (int i = minJump; i <= maxJump; i++)
            {
                var nextIndex = index + i;
                if (nextIndex == s.Length - 1 && s[nextIndex] == '0') return true;
                if (nextIndex < s.Length && s[nextIndex] == '0' && visited[nextIndex] == 0)
                {
                    visited[nextIndex] = 1;
                    queue.Enqueue(nextIndex);
                    continue;
                }
                if (nextIndex >= s.Length) break;
            }
        }
        return false;
    }

    public bool CanReachDFS(string s, int minJump, int maxJump)
    {
        if (s[s.Length - 1] == '1') return false;
        var visited = new int[s.Length];
        static bool HelperDFS(string s, int minJump, int maxJump, ref int[] visited, int index)
        {
            if (index >= s.Length || s[index] == '1' || visited[index] == 1) return false;
            if (index == s.Length - 1 && s[index] == '0') return true;
            visited[index] = 1;
            for (int i = maxJump; i >= minJump; i--)
            {
                var found = HelperDFS(s, minJump, maxJump, ref visited, index + i);
                if (found) return true;
            }
            return false;
        }
        return HelperDFS(s, minJump, maxJump, ref visited, 0);
    }

    public bool CanReachDP(string s, int minJump, int maxJump)
    {
        int n = s.Length;
        if (s[n - 1] == '1') return false;
        var dp = new bool[n];
        dp[0] = true;
        int canReachCount = 0;
        for (int i = 1; i < n; i++)
        {
            if (i - minJump >= 0 && dp[i - minJump])
            {
                canReachCount++;
            }
            if (i - maxJump - 1 >= 0 && dp[i - maxJump - 1])
            {
                canReachCount--;
            }
            if (canReachCount > 0 && s[i] == '0')
            {
                dp[i] = true;
            }
        }
        return dp[n - 1];
    }
}
