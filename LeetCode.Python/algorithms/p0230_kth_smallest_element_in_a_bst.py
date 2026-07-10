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
    
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        counter = 0
        stack = []
        def next() -> int:
            nonlocal counter
            if counter == 0:
                cp = root
                while cp is not None:
                    stack.append(cp)
                    cp = cp.left
            p = stack.pop()
            cp = p.right
            while cp is not None:
                stack.append(cp)
                cp = cp.left
            counter += 1
            return p.val
        for i in range(k):
            if i == k - 1:
                return next()
            else:
                next()
        return -1