namespace LeetCode.CSharp.Algorithms;

public class _0009_PalindromeNumber
{
    public bool IsPalindrome(int x) 
    {
        string xString = x.ToString();
        for (int i = 0; i < xString.Length / 2; i++)
        {
            if (xString[i] != xString[xString.Length - 1 - i])
            {
                return false;
            }
        }
        return true;
    }

    public bool IsPalindromeWithoutString(int x)
    {
        if (x < 0 || (x != 0 && x % 10 == 0))
        {
            return false;
        }
        int reversedHalf = 0;
        int originalInt = x;
        while (x > reversedHalf)
        {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        return x == reversedHalf || x == reversedHalf / 10;
    }
}