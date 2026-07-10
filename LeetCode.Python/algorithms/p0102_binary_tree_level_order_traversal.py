from collections import deque

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
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        answer = []
        if root is None:
            return answer
        l1 = [root]
        while l1:
            l2 = []
            temp_l = []
            for n in l1:
                temp_l.append(n.val)
                if n.left is not None:
                    l2.append(n.left)
                if n.right is not None:
                    l2.append(n.right)
            answer.append(temp_l)
            l1 = l2
        return answer
    
    def levelOrderQueue(self, root: TreeNode | None) -> list[list[int]]:
        answer = []
        if root is None:
            return answer
        queue = deque([root])
        while queue:
            level_size = len(queue)
            temp_l = []
            for _ in range(level_size):
                node = queue.popleft()
                temp_l.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            answer.append(temp_l)
        return answer