using System.Text;

namespace LeetCode.CSharp.Algorithms;

public class _0014_LongestCommonPrefix
{
    // First attempt — kept for reference. See LongestCommonPrefix2 for the cleaner version
    // (plain for-loop, early-return Substring on mismatch, no StringBuilder/flag).
    public string LongestCommonPrefix(string[] strs)
    {
        if ( strs.Length == 0 )
        {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        int i = 0;
        bool flag = true;
        while (true) {
            if ( i > strs[0].Length - 1) break;
            char c = strs[0][i];
            for (int j = 1; j < strs.Length; j++) {
                string s = strs[j];
                if ((i > s.Length - 1) || (c != s[i]))
                {
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
            sb.Append(c);
            i++;
        }
        return sb.ToString();
    }

    public string LongestCommonPrefix2(string[] strs)
    {
        if (strs.Length == 0) return "";
        for (int i = 0; i < strs[0].Length; i++)
        {
            char c = strs[0][i];
            for (int j = 1; j < strs.Length; j++)
            {
                if (i >= strs[j].Length || c != strs[j][i])
                {
                    return strs[0][..i];
                }
            }
        }
        return strs[0];
    }
}
