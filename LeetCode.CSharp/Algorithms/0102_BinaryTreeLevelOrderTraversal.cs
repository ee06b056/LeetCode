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

public class _0102_BinaryTreeLevelOrderTraversal
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

    public IList<IList<int>> LevelOrder(TreeNode root)
    {
        var wholeList = new List<IList<int>>();
        if (root == null) return wholeList;
        var queue1 = new Queue<TreeNode>();
        var queue2 = new Queue<TreeNode>();
        queue1.Enqueue(root);
        while (queue1.Count > 0)
        {
            var levelList = new List<int>();
            while (queue1.Count > 0)
            {
                var node = queue1.Dequeue();
                levelList.Add(node.val);
                if (node.left != null) queue2.Enqueue(node.left);
                if (node.right != null) queue2.Enqueue(node.right);
            }
            (queue1, queue2) = (queue2, queue1);
            wholeList.Add(levelList);
        }
        return wholeList;
    }

    public IList<IList<int>> LevelOrder2(TreeNode root)
    {
        var wholeList = new List<IList<int>>();
        if (root == null) return wholeList;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0)
        {
            var levelList = new List<int>();
            int count = q.Count;
            wholeList.Add(levelList);
            for (int i = 0; i < count; i++)
            {
                var node = q.Dequeue();
                levelList.Add(node.val);
                if (node.left != null)
                {
                    q.Enqueue(node.left);
                }
                if (node.right != null) q.Enqueue(node.right);
            }
        }
        return wholeList;
    }

    public IList<IList<int>> LevelOrderRecursive(TreeNode root)
    {
        static void Helper(TreeNode node, int level, List<IList<int>> wholeList)
        {
            if (node == null) return;
            if (level > wholeList.Count)
            {
                wholeList.Add(new List<int>());
            }
            wholeList[level - 1].Add(node.val);
            Helper(node.left, level + 1, wholeList);
            Helper(node.right, level + 1, wholeList);
        }
        var wholeList = new List<IList<int>>();
        Helper(root, 1, wholeList);
        return wholeList;
    }
}
