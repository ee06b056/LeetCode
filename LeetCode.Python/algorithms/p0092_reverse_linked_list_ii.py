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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left == right:
            return head
        dummy = ListNode(next=head)
        cp = dummy
        i = 0
        while i < left - 1:
            cp = cp.next
            i += 1
        pre_left = cp
        tail = cp.next
        np = cp.next
        while i < right:
            i += 1
            n_temp = np.next
            np.next = cp
            pre_left.next = np
            cp = np
            np = n_temp
        tail.next = np
        return dummy.next
    