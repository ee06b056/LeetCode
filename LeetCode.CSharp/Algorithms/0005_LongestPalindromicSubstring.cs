using System;

namespace LeetCode.CSharp.Algorithms;

public class _0005_LongestPalindromicSubstring
{
    public string LongestPalindrome(string s)
    {
        int maxLength = 1;
        string answer = s[..1];
        for (int i = 0; i < s.Length; i++)
        {
            int even = Expand(s, i, i + 1);
            int odd = Expand(s, i , i);
            int l = Math.Max(even, odd);
            if (maxLength < l)
            {
                maxLength = l;
                answer = s.Substring(i - (l - 1) / 2, l);
            }
        }
        return answer;
    }

    public static int Expand(string s, int left, int right)
    {
        int l = 0;
        while (left >= 0 && right < s.Length && s[left] == s[right])
        {
            l = right - left + 1;
            left--;
            right++;
        }
        return l;
    }
}
