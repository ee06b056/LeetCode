"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        dq = deque()
        node_dict = {}
        start_node = Node(node.val)
        node_dict[node.val] = start_node
        dq.append(node)
        while dq:
            cnode = dq.popleft()
            new_cnode = node_dict[cnode.val]
            for nnode in cnode.neighbors:
                if nnode.val not in node_dict:
                    new_nnode = Node(nnode.val)
                    node_dict[nnode.val] = new_nnode
                    dq.append(nnode)
                new_cnode.neighbors.append(node_dict[nnode.val])
        return start_node