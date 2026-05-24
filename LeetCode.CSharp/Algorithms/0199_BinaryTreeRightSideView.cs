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

public class _0199_BinaryTreeRightSideView
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
    }

    public IList<int> RightSideView(TreeNode root)
    {
        var rightSideView = new List<int>();
        var queue = new Queue<TreeNode>();
        if (root == null) return rightSideView;
        queue.Enqueue(root);
        while (queue.Count > 0)
        {
            int count = queue.Count;
            for (int i = 0; i < count; i++)
            {
                var currentNode = queue.Dequeue();
                if (i == count - 1) rightSideView.Add(currentNode.val);
                if (currentNode.left != null) queue.Enqueue(currentNode.left);
                if (currentNode.right != null) queue.Enqueue(currentNode.right);
            }
        }
        return rightSideView;
    }
}
