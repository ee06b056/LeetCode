using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0020_ValidParenthese
{
    public bool IsValid(string s)
    {
        Stack<char> stack = new();
        char top;
        foreach (char c in s) {
            switch (c)
            {
                case '{':
                case '[':
                case '(':
                    stack.Push(c);
                    break;
                case '}':
                    if (!stack.TryPop(out top) || top != '{') return false;
                    break;
                case ']':
                    if (!stack.TryPop(out top) || top != '[') return false;
                    break;
                case ')':
                    if (!stack.TryPop(out top) || top != '(') return false;
                    break;
            }
        }
        return stack.Count == 0;
    }
}
