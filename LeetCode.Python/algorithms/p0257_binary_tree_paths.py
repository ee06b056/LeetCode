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
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        answer = []
        if root is None:
            return answer
        path = []
        def dfs(node: TreeNode | None, path: list) -> None:
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                answer.append("->".join(str(i) for i in path))
            if node.left is not None:
                dfs(node.left, path)
            if node.right is not None:
                dfs(node.right, path)   
            path.pop()
            return
        dfs(root, path)
        return answer
    
    def binaryTreePathsIterative(self, root: TreeNode | None) -> list[str]:
        if root is None:
            return []
        answer = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                answer.append("->".join(str(i) for i in path))
            if node.right is not None:
                stack.append((node.right, path + [node.right.val]))
            if node.left is not None:
                stack.append((node.left, path + [node.left.val]))
        return answer