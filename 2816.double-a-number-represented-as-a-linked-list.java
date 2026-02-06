#
# @lc app=leetcode id=2816 lang=java
#
# [2816] Double a Number Represented as a Linked List
#
# @lc code=start
/**
* Definition for singly-linked list.
* public class ListNode {
*     int val;
*     ListNode next;
*     ListNode() {}
*     ListNode(int val) { this.val = val; }
*     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
* }
*/
class Solution {
    public ListNode doubleIt(ListNode head) {
        head = reverse(head);
        ListNode curr = head;
        int carry = 0;
        ListNode prev = null;
        while (curr != null) {
            int sum = curr.val * 2 + carry;
            curr.val = sum % 10;
            carry = sum / 10;
            prev = curr;
            curr = curr.next;
        }
        if (carry > 0) {
            prev.next = new ListNode(carry);
        }
        return reverse(head);
    }
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}
# @lc code=end