using System.Text;

namespace LeetCode.CSharp.Algorithms;

public class _0014_LongestCommonPrefix
{
    // TODO: revisit — algorithm is correct O(n*m) vertical scan, but the StringBuilder + `flag` pattern can be cleaner:
    //   use a plain for-loop, early-return strs[0].Substring(0, i) on mismatch, drop the flag entirely.
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
}
