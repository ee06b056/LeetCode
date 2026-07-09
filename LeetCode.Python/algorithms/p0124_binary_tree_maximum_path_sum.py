# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def helper(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return 0, float("-inf")
            left_b, left_p = helper(node.left)
            right_b, right_p = helper(node.right)
            b = max(0, node.val + max(left_b, right_b))
            p = max(left_p, right_p, node.val + left_b + right_b)
            return b, p
        _, p = helper(root)
        return p