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
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if root is None:
            return []
        answer = []
        path = []
        def dfs(node: TreeNode, path_sum: int) -> None:
            path_sum += node.val
            path.append(node.val)
            if node.left is None and node.right is None and path_sum == targetSum:
                answer.append(path[:])
            if node.left is not None:
                dfs(node.left, path_sum)
            if node.right is not None:
                dfs(node.right, path_sum)
            path.pop()
        dfs(root, 0)
        return answer