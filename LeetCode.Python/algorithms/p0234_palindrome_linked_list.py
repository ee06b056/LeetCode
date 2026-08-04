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
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True
        fast, slow = head, head
        while fast is not None:
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            slow = slow.next
        pre, cur = None, slow
        while cur is not None:
            n_temp = cur.next
            cur.next = pre
            pre = cur
            cur = n_temp
        p1, p2 = head, pre
        while p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True