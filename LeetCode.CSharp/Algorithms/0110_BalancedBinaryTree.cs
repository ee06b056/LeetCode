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

public class _0110_BalancedBinaryTree
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
    }

    public bool IsBalanced(TreeNode root)
    {
        static int HeightHelper(TreeNode node, ref bool isBalanced)
        {
            if (node == null || !isBalanced) return 0;
            int leftHeight= HeightHelper(node.left, ref isBalanced);
            int rightHeight = HeightHelper(node.right, ref isBalanced);
            if (Math.Abs(leftHeight - rightHeight) > 1)
            {
                isBalanced = false;
                return 0;
            }
            return 1 + Math.Max(leftHeight, rightHeight);
        }
        var isBalanced = true;
         _ = HeightHelper(root, ref isBalanced);
        return isBalanced;
    }
}
