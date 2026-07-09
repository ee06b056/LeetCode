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
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        def helper(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return (0, 0)
            left_h, left_d = helper(node.left)
            right_h, right_d = helper(node.right)
            h = 1+ max(left_h, right_h)
            d = max(left_h + right_h, max(left_d, right_d))
            return (h, d)
        _, d = helper(root)
        return d