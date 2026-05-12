using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0013_RomanToInteger
{
    public int RomanToInt(string s)
    {
        int result = 0;
        Dictionary<string, int> dict = new()
        {
            { "I", 1 },
            { "V", 5 },
            { "X", 10 },
            { "L", 50 },
            { "C", 100 },
            { "D", 500 },
            { "M", 1000 },
            { "IV", 4 },
            { "IX", 9 },
            { "XL", 40 },
            { "XC", 90 },
            { "CD", 400 },
            { "CM", 900 }
        };
        for (int i = 0; i < s.Length; i++)
        {
            if (i + 1 < s.Length && dict.ContainsKey(s.Substring(i, 2)))
            {
                result += dict.GetValueOrDefault(s.Substring(i, 2));
                i++;
            }
            else
            {
                result += dict.GetValueOrDefault(s.Substring(i, 1));
            }
        }
        return result;
    }

    public int RomanToInt2(string s)
    {
        int result = 0;
        Dictionary<char, int> dict = new()
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
        int currentValue = dict.GetValueOrDefault(s[0]);
        for (int i = 1; i < s.Length; i++) 
        {
            int nextValue = dict.GetValueOrDefault(s[i]);
            if (currentValue < nextValue) 
            {
                result -= currentValue;
            }
            else
            {
                result += currentValue;
            }
            currentValue = nextValue;
        }
        result += currentValue;
        return result;
    }

    public int RomanToInt3(string s)
    {
        int result = 0;
        Dictionary<char, int> dict = new()
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
        int prevValue = 0;
        for (int i = s.Length - 1; i >= 0; i--)
        {
            int currentValue = dict[s[i]];
            if (currentValue < prevValue)
            {
                result -= currentValue;
            }
            else
            {
                result += currentValue;
            }
            prevValue = currentValue;
        }
        return result;
    }
}
