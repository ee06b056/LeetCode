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
    def isBalanced(self, root: TreeNode | None) -> bool:
        def isBalancedHelper(node: TreeNode | None) -> int:
            if node is None:
                return 0
            lh = isBalancedHelper(node.left)
            rh = isBalancedHelper(node.right)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return max(lh, rh) + 1
        return isBalancedHelper(root) != -1
