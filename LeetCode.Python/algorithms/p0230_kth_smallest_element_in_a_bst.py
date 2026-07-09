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
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        topk = []
        def inorder(node: TreeNode | None) -> None:
            if len(topk) >= k:
                return
            if node is None:
                return
            inorder(node.left)
            if len(topk) >= k:
                return
            topk.append(node.val)
            inorder(node.right)
            return
        inorder(root)
        return topk[k - 1]