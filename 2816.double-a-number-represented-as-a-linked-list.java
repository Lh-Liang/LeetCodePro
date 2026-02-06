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
        if (head == null) return null;
        int carry = 0;
        ListNode current = head;
        while (current != null) {
            int doubledValue = current.val * 2 + carry;
            current.val = doubledValue % 10;
            carry = doubledValue / 10;
            if (current.next == null && carry > 0) {
                current.next = new ListNode(carry);
                break; // No need to continue since we just appended last node. 
            } 
            current = current.next; 
        } 
        return head; 
    } 
}
# @lc code=end