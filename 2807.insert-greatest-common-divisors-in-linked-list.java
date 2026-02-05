#
# @lc app=leetcode id=2807 lang=java
#
# [2807] Insert Greatest Common Divisors in Linked List
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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if (head == null || head.next == null) { return head; }
        ListNode current = head;
        while (current != null && current.next != null) {
            int gcdValue = gcd(current.val, current.next.val);
            ListNode newNode = new ListNode(gcdValue);
            newNode.next = current.next;
            current.next = newNode;
            current = newNode.next; // Move two steps forward in the list.
            // Verification step: Check if new node is correctly placed.
            assert current != null : "Insertion error: Current node is null.";
            assert current.val == gcd(newNode.val, current.val) : "GCD value incorrect.";
        }
        return head;
    }
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b; 
            b = a % b; 
            a = temp; 
        } 
        return a; 
    } 
}
# @lc code=end