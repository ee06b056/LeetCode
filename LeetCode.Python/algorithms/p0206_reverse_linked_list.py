# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        p1.next = None
        while p2.next is not None:
            temp_p = p2.next
            p2.next = p1
            p2, p1 = temp_p, p2
        p2.next = p1
        return p2
    
    def reverseListRecursive(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head