# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        node_set = set()
        p = head
        while p:
            if p in node_set:
                return True
            node_set.add(p)
            p = p.next
        return False
    
    def hasCycleDoublePointer(self, head: ListNode | None) -> bool:
        if head is None:
            return False
        slow_p = head
        fast_p = head
        while fast_p is not None and fast_p.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p is fast_p:
                return True
        return False