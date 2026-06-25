# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cp = dummy
        while cp.next is not None and cp.next.next is not None:
            p1 = cp.next
            p2 = p1.next
            next_p = p2.next
            cp.next = p2
            p2.next = p1
            p1.next = next_p
            cp = p1
        return dummy.next
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p1, p2 = head.next, head.next.next
        p1.next = head
        head.next = self.swapPairs(p2)
        return p1