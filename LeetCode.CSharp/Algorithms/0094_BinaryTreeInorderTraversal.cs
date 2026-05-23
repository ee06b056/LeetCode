
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

public class _0094_BinaryTreeInorderTraversal
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

    public IList<int> InorderTraversal(TreeNode root) {
        if (root == null) return new List<int>();
        List<int> inorderList = new();
        inorderList.AddRange(InorderTraversal(root.left));
        inorderList.Add(root.val);
        inorderList.AddRange(InorderTraversal(root.right));
        return inorderList;
    }

    public IList<int> InorderTraversalIterative(TreeNode root) 
    {
        var inorderList = new List<int>();
        if (root == null) return inorderList;
        var p = root;
        var stack = new Stack<TreeNode>();
        while(p != null)
        {
            stack.Push(p);
            p = p.left;
        }
        while(stack.Count != 0)
        {
            var cp = stack.Pop();
            inorderList.Add(cp.val);
            cp = cp.right;
            while(cp != null)
            {
                stack.Push(cp);
                cp = cp.left;
            }
        }
        return inorderList;
    }

    public IList<int> InorderTraversalInterative2(TreeNode root)
    {
        var inorderList = new List<int>();
        var currentNode = root;
        var stack = new Stack<TreeNode>();
        while(currentNode != null || stack.Count > 0)
        {
            while (currentNode != null)
            {
                stack.Push(currentNode);
                currentNode = currentNode.left;
            }
            currentNode = stack.Pop();
            inorderList.Add(currentNode.val);
            currentNode = currentNode.right;
        }
        return inorderList;
    }
}
