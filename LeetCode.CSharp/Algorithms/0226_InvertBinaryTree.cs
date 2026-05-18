using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

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

public class _0226_InvertBinaryTree
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        
    }

    public TreeNode InvertTree(TreeNode root) 
    {
        if (root == null) return null;
        TreeNode leftNode = root.left, rightNode = root.right;
        root.left = InvertTree(rightNode);
        root.right = InvertTree(leftNode);
        return root;
    }

    public TreeNode InvertTreeDFS(TreeNode root) 
    {
        if (root == null) return null;
        Stack<TreeNode> stack = new();
        stack.Push(root);
        while (stack.Count > 0)
        {
            TreeNode cp = stack.Pop();
            (cp.left, cp.right) = (cp.right, cp.left);
            if(cp.left != null) stack.Push(cp.left);
            if(cp.right != null) stack.Push(cp.right);
        }
        return root;
    }
}
