using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0542_01Matrix
{
    public int[][] UpdateMatrix(int[][] mat)
    {
        int m = mat.Length, n = mat[0].Length;
        int[][] distanceMatrix = new int[m][];
        int[][] directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for (int i = 0; i < m; i++)
        {
            distanceMatrix[i] = new int[n];
        }
        var visitedSet = new HashSet<(int, int)>();
        var cellQueue = new Queue<(int, int, int)>();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 0)
                {
                    cellQueue.Enqueue((i, j, 0));
                    visitedSet.Add((i, j));
                }
            }
        }
        while (cellQueue.Count != 0)
        {
            var (i, j, v) = cellQueue.Dequeue();
            foreach (int[] direction in directions)
            {
                var (nextI, nextJ) = (i + direction[0], j + direction[1]);
                if (nextI >= 0 && nextI < m && nextJ >= 0 && nextJ < n && visitedSet.Add((nextI, nextJ)))
                {
                    distanceMatrix[nextI][nextJ] = v + 1;
                    cellQueue.Enqueue((nextI, nextJ, v + 1));
                }
            }
        }
        return distanceMatrix;
    }

    public int[][] UpdateMatrix2(int[][] mat)
    {
        int m = mat.Length, n = mat[0].Length;
        var distMat = new int[m][];
        var cellQ = new Queue<(int, int)>(m * n);
        int[][] directions = [[1, 0], [-1, 0], [0, -1], [0, 1]];
        for (int i = 0; i < m; i++)
        {
            distMat[i] = new int[n];
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 0)
                {
                    distMat[i][j] = 0;
                    cellQ.Enqueue((i, j));
                }
                else
                {
                    distMat[i][j] = -1;
                }
            }
        }
        while(cellQ.Count != 0)
        {
            var (i , j) = cellQ.Dequeue();
            int v = distMat[i][j];
            foreach (int[] direction in directions)
            {
                var (nextI, nextJ) = (i + direction[0], j + direction[1]);
                if (nextI >= 0 && nextI < m && nextJ >= 0 && nextJ < n && distMat[nextI][nextJ] == -1)
                {
                    cellQ.Enqueue((nextI, nextJ));
                    distMat[nextI][nextJ] = v + 1;
                }
            }
        }
        return distMat;
    }

    public int[][] UpdateMatrixDP(int[][] mat)
    {
        int m = mat.Length, n = mat[0].Length;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 1)
                {
                    mat[i][j] = m + n;
                }
            }
        }
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 0) continue;
                if (i - 1 >= 0) mat[i][j] = Math.Min(mat[i][j], mat[i - 1][j] + 1);
                if (j - 1 >= 0) mat[i][j] = Math.Min(mat[i][j], mat[i][j - 1] + 1);
            }
        }
        for (int i = m - 1; i >= 0; i--)
        {
            for (int j = n  - 1; j >= 0; j--)
            {
                if (mat[i][j] == 0) continue;
                if (i + 1 < m) mat[i][j] = Math.Min(mat[i][j], mat[i + 1][j] + 1);
                if (j + 1 < n) mat[i][j] = Math.Min(mat[i][j], mat[i][j + 1] + 1);
            }
        }
        return mat;
    }
}
