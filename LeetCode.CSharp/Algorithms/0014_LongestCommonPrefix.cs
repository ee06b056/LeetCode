using System.Text;

namespace LeetCode.CSharp.Algorithms;

public class _0014_LongestCommonPrefix
{
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
