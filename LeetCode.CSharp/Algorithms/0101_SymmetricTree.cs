/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0101_SymmetricTree
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public bool IsSymmetric(TreeNode root)
    {
        static bool Helper(TreeNode nodeleft, TreeNode noderight)
        {
            if (nodeleft == null && noderight == null) return true;
            if (nodeleft != null && noderight != null && nodeleft.val == noderight.val)
            {
                return Helper(nodeleft.left, noderight.right) && Helper(nodeleft.right, noderight.left);
            }
            return false;
        }
        return Helper(root.left, root.right);
    }

    public bool IsSymmetricIteractive(TreeNode root)
    {
        var leftStack = new Stack<TreeNode>();
        var rightStack = new Stack<TreeNode>();
        leftStack.Push(root.left);
        rightStack.Push(root.right);
        while (leftStack.Count > 0 && rightStack.Count > 0)
        {
            var left = leftStack.Pop();
            var right = rightStack.Pop();
            if (left == null && right == null) continue;
            if (left != null && right != null && left.val == right.val)
            {
                leftStack.Push(left.left);
                rightStack.Push(right.right);
                leftStack.Push(left.right);
                rightStack.Push(right.left);
            }
            else
            {
                return false;
            }
        }
        return leftStack.Count == 0 && rightStack.Count == 0;
    }
}
