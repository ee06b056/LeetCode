namespace LeetCode.CSharp.Algorithms;

public class _0125_ValidPalindrome
{
    public bool IsPalindrome(string s)
    {
        int i = 0, j = s.Length - 1;
        while (i < j)
        {
            if (!char.IsAsciiLetterOrDigit(s[i]))
            {
                i++;
            }
            else if (!char.IsAsciiLetterOrDigit(s[j]))
            {
                j--;
            }
            else if (char.ToLowerInvariant(s[i]) != char.ToLowerInvariant(s[j]))
            {
                return false;
            }
            else
            {
                i++;
                j--;
            }
        }
        return true;
    }
}
