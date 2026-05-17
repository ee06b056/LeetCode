using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0003_LongestSubstringWithoutRepeatingCharacters {
    public int LengthOfLongestSubstring(string s)
    {
        int longestLength = 0;
        int i = 0;
        HashSet<char> charSet = new(); 
        for (int j = 0; j < s.Length; j++)
        {
            if (!charSet.Contains(s[j]))
            {
                longestLength = Math.Max(longestLength, j - i + 1);
            }
            else
            {
                while (charSet.Contains(s[j]))
                {
                    charSet.Remove(s[i]);
                    i++;
                }
            }
            charSet.Add(s[j]);
        }
        return longestLength;
    }

    public int LengthOfLongestSubstring2(string s)
    {
        int longestLength = 0;
        int k = -1; 
        Dictionary<char, int> charIndexMap = new();
        for (int j = 0; j < s.Length; j++)
        {
            if (charIndexMap.TryGetValue(s[j], out int index))
            {
                k = Math.Max(k, index);
            }
            charIndexMap[s[j]] = j;
            longestLength = Math.Max(longestLength, j - k);
        }
        return longestLength;
    }
}
