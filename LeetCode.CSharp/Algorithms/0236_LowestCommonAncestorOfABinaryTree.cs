/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */

namespace LeetCode.CSharp.Algorithms;

public class _0236_LowestCommonAncestorOfABinaryTree
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
    }

    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        static int FindHelper(TreeNode node, TreeNode p, TreeNode q, ref TreeNode LCA)
        {
            if (LCA != null) return 0;
            if (node == null) return -1;
            int leftFound = FindHelper(node.left, p, q, ref LCA);
            int rightFound = FindHelper(node.right, p, q, ref LCA);
            if (leftFound == -1 && rightFound == -1)
            {
                return (node.val == p.val || node.val == q.val) ? 1 : -1;
            }
            else if (leftFound == 1 && rightFound == 1)
            {
                LCA = node;
                return 0;
            }
            else if (node.val != p.val && node.val != q.val)
            {
                return 1;
            }
            else{
                LCA = node;
                return 0;
            }
        }
        TreeNode LCA = null;
        FindHelper(root, p, q, ref LCA);
        return LCA;
    }

    public TreeNode LowestCommonAncestor2(TreeNode root, TreeNode p, TreeNode q)
    {
        if (root == null || root.val == p.val || root.val == q.val) return root;
        var left = LowestCommonAncestor(root.left, p, q);
        var right = LowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left ?? right;
    }
}