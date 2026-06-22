using System.Text;

namespace LeetCode.CSharp.Algorithms;

public class _0012_IntegerToRoman
{
    public string IntToRoman(int num)
    {
        (int value, string symbol)[] table = 
        [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ];
        var sb = new StringBuilder();
        foreach ((int value, string symbol) in table)
        {
            while (num >= value)
            {
                sb.Append(symbol);
                num -= value;
            }
        }
        return sb.ToString();
    }
}
