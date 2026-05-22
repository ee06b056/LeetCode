using System;
using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0104_MaximumDepthOfBinaryTree
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int MaxDepth(TreeNode root)
    {
        int depth = 0;
        if (root == null) return depth;
        var q1 = new Queue<TreeNode>();
        var q2 = new Queue<TreeNode>();
        q1.Enqueue(root);
        while (q1.Count != 0)
        {
            while(q1.Count != 0)
            {
                var p = q1.Dequeue();
                if (p.left != null) q2.Enqueue(p.left);
                if (p.right != null) q2.Enqueue(p.right);
            }
            depth++;
            (q1, q2) = (q2, q1);
        }
        return depth;
    }

    public int MaxDepth2(TreeNode root)
    {
        if (root == null) return 0;
        int leftDepth = MaxDepth2(root.left);
        int rightDepth = MaxDepth2(root.right);
        return Math.Max(leftDepth, rightDepth) + 1;
    }
}
