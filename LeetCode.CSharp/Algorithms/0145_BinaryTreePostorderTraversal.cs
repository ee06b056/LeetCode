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

public class _0145_BinaryTreePostorderTraversal
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

    public IList<int> PostorderTraversal(TreeNode root)
    {
        if (root == null) return new int[0];
        var postorderList = new List<int>();
        postorderList.AddRange(PostorderTraversal(root.left));
        postorderList.AddRange(PostorderTraversal(root.right));
        postorderList.Add(root.val);
        return postorderList;
    }

    public IList<int> PostorderTraversalIterative(TreeNode root)
    {
        if (root == null) return new int[0];
        var postorderList = new List<int>();
        var stack = new Stack<TreeNode>();
        stack.Push(root);
        while (stack.Count > 0)
        {
            var node = stack.Pop();
            postorderList.Add(node.val);
            if (node.left != null)
            {
                stack.Push(node.left);
            }
            if (node.right != null)
            {
                stack.Push(node.right);
            }
        }
        postorderList.Reverse();
        return postorderList;
    }
}
