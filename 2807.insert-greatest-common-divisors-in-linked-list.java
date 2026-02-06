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
import java.util.*; 
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) { 
        if (head == null || head.next == null) return head; 
        ListNode current = head; 
        while (current != null && current.next != null) { 
            int gcdValue = gcd(current.val, current.next.val); 
            ListNode gcdNode = new ListNode(gcdValue); 
            gcdNode.next = current.next; 
            current.next = gcdNode; 
            current = gcdNode.next; 
        } 
        return head; 
    } 
    private int gcd(int a, int b) { 
        if (b == 0) return a; 
        return gcd(b, a % b); 
    } 
}
# @lc code=end