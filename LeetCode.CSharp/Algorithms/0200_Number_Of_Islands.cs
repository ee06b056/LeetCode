using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0200_Number_Of_Islands
{
    public int NumIslands(char[][] grid)
    {
        if (grid.Length == 0 || grid[0].Length == 0) return 0;
        int islandCount = 0;
        int m = grid.Length, n = grid[0].Length;
        var directs = new (int, int)[] { (1, 0), (-1, 0), (0, 1), (0, -1) };
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == '1')
                {
                    islandCount += 1;
                    var q = new Queue<(int, int)>();
                    q.Enqueue((i, j));
                    grid[i][j] = '0';
                    while(q.Count > 0)
                    {
                        var (r, c) = q.Dequeue();
                        foreach (var (mr, mc) in directs)
                        {
                            int nr = r + mr, nc = c + mc;
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1')
                            {
                                q.Enqueue((nr, nc));
                                grid[nr][nc] = '0';
                            }
                        }
                    }
                }
            }
        }
        return islandCount;
    }
}
