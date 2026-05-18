using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0242_ValidAnagram
{
    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length) return false;
        var charDict = new Dictionary<char, int>();
        foreach (char c in s)
        {
            if(charDict.TryGetValue(c, out int i))
            {
                charDict[c] = ++i;
            }
            else
            {
                charDict[c] = 1;
            }
        }
        foreach (char c in t)
        {
            if (charDict.TryGetValue(c, out int i) && i > 0)
            {
                charDict[c] = --i;
            }
            else
            {
                return false;
            }
        }
        return true;
    }

    public bool IsAnagram2(string s, string t)
    {
        if (s.Length != t.Length) return false;
        int[] countArr = new int[26];
        foreach (char c in s)
        {
            countArr[c - 97]++;
        }
        foreach (char c in t)
        {
            if (countArr[c - 97] == 0) return false;
            countArr[c - 97]--;
        }
        return true;
    }
}
