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

using System;

namespace LeetCode.CSharp.Algorithms;

public class _0543_DiameterOfBinaryTree
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

    public int DiameterOfBinaryTree(TreeNode root)
    {
        static (int, int) Helper(TreeNode node)
        {
            if (node == null) return (0, 0);
            var (leftpath, leftdiameter) = Helper(node.left);
            var (rightpath, rightdiameter) = Helper(node.right);
            return (Math.Max(leftpath + 1, rightpath + 1), Math.Max((leftpath + rightpath), Math.Max(leftdiameter, rightdiameter)));
        }
        var (_, diameter) = Helper(root);
        return diameter;
    }

    public int DiameterOfBinaryTreeRef(TreeNode root)
    {
        int diameter = 0;
        static int Helper(TreeNode node, ref int diameter)
        {
            if (node == null) return 0;
            int leftPath = Helper(node.left, ref diameter);
            int rightPath = Helper(node.right, ref diameter);
            diameter = Math.Max(leftPath + rightPath, diameter);
            return 1 + Math.Max(leftPath, rightPath);
        }
        Helper(root, ref diameter);
        return diameter;
    }
}
