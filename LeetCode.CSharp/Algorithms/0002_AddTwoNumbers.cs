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

public class _0002_AddTwoNumbers
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val=0, ListNode next=null)
        {
            this.val = val;
            this.next = next;
        }
    }
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        var startNode = new ListNode();
        var p = startNode;
        int carry =0;
        while (l1 != null || l2 != null || carry != 0)
        {
            int v1 = l1 == null? 0 : l1.val;
            int v2 = l2 == null? 0 : l2.val;
            int sum = v1 + v2 + carry;
            carry = sum / 10;
            p.next = new ListNode(sum % 10);
            p = p.next;
            l1 = l1?.next;
            l2 = l2?.next;
        }
        return startNode.next;
    }

    public ListNode AddTwoNumbers2(ListNode l1, ListNode l2)
    {
        return AddTwoNumbersRecursive(l1, l2);
    }

    public ListNode AddTwoNumbersRecursive(ListNode l1, ListNode l2, int carry = 0)
    {
        if (l1 == null && l2 == null && carry == 0) return null;
        int v1 = l1 == null ? 0 : l1.val;
        int v2 = l2 == null ? 0 : l2.val;
        int sum = v1 + v2 + carry;
        var node = new ListNode(sum % 10);
        node.next = AddTwoNumbersRecursive(l1?.next, l2?.next, sum / 10);
        return node;
    }

}
