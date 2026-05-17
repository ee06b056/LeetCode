namespace LeetCode.CSharp.Algorithms;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class _0021_MergeTwoSortedLists
{
    public class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}
    public ListNode MergeTwoLists(ListNode list1, ListNode list2)
    {
        ListNode head = new();
        ListNode p1 = list1, p2 = list2, cp = head;
        while (p1 != null && p2 != null) 
        {
            if (p1.val >= p2.val) 
            {
                cp.next = p2;
                p2 = p2.next;
            } 
            else 
            {
                cp.next = p1;
                p1 = p1.next;
            }
            cp = cp.next;
        }
        cp.next = p1 ?? p2;
        return head.next;
    }
}
