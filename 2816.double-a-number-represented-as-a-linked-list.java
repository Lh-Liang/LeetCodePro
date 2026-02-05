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
        
        // Reverse the linked list to handle carries from least significant digit.
        head = reverseList(head);
        
        ListNode current = head;
        int carry = 0;
        
        while (current != null) {
            int newValue = current.val * 2 + carry; // Double current digit and add carry.
            current.val = newValue % 10; // Update current node with new value modulo 10.
            carry = newValue / 10; // Calculate new carry.
            
            if (current.next == null && carry > 0) { // If at end and still have carry, add new node.
                current.next = new ListNode(carry);
                break; // No further processing needed once carry is accommodated.
            } else { 
                current = current.next; // Move to next node if exists. 
            } 
        } 
      	// Reverse back to original order before returning. 	
      head = reverseList(head); 		return head; 	}	private ListNode reverseList(ListNode head) { 		ListNode prev = null; 		while (head != null) { 			ListNode nextTemp = head.next; 			head.next = prev; 			prev = head; 			head = nextTemp; 		} return prev;} } # @lc code=end