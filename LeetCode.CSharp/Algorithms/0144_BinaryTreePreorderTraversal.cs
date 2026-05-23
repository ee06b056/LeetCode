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

public class _0144_BinaryTreePreorderTraversal
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

    public IList<int> PreorderTraversal(TreeNode root)
    {
        if (root == null) return new int[0];
        var preorderList = new List<int>{ root.val };
        preorderList.AddRange(PreorderTraversal(root.left));
        preorderList.AddRange(PreorderTraversal(root.right));
        return preorderList;
    }

    public IList<int> PreorderTraversalRecursive(TreeNode root)
    {
        static void Helper(TreeNode node, List<int> list)
        {
            if (node == null) return;
            list.Add(node.val);
            Helper(node.left, list);
            Helper(node.right, list);
        }
        var preorderList = new List<int>();
        Helper(root, preorderList);
        return preorderList;
    }

    public IList<int> PreorderTraversalIterative(TreeNode root)
    {
        var currentNode = root;
        var stack = new Stack<TreeNode>();
        var preorderList = new List<int>();
        while (currentNode != null || stack.Count > 0)
        {
            while(currentNode != null)
            {
                preorderList.Add(currentNode.val);
                stack.Push(currentNode);
                currentNode = currentNode.left;
            }
            currentNode = stack.Pop();
            currentNode = currentNode.right;
        }
        return preorderList;
    }
}
