using System;

namespace LeetCode.CSharp.Algorithms;

public class _0165_CompareVersionNumbers
{
    public int CompareVersion(string version1, string version2)
    {
        ReadOnlySpan<char> v1 = version1;
        ReadOnlySpan<char> v2 = version2;

        while (!v1.IsEmpty || !v2.IsEmpty)
        {
            int r1 = NextRevision(ref v1);
            int r2 = NextRevision(ref v2);
            if (r1 < r2) return -1;
            if (r1 > r2) return 1;
        }
        return 0;
    }

    private static int NextRevision(ref ReadOnlySpan<char> version)
    {
        if (version.IsEmpty) return 0;

        int dot = version.IndexOf('.');
        ReadOnlySpan<char> revision;
        if (dot < 0)
        {
            revision = version;
            version = ReadOnlySpan<char>.Empty;
        }
        else
        {
            revision = version[..dot];
            version = version[(dot + 1)..];
        }

        return int.Parse(revision);
    }
}
