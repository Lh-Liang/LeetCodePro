#
# @lc app=leetcode id=3217 lang=java
#
# [3217] Delete Nodes From Linked List Present in Array
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
import java.util.HashSet;
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) { 
            numSet.add(num); 
        } 
        
        ListNode dummy = new ListNode(0); 
        dummy.next = head; 
        ListNode prev = dummy; 
        
        while (head != null) { 
            if (numSet.contains(head.val)) { 
                prev.next = head.next; 
            } else { 
                prev = head; 
            } 
            head = head.next; 
        } 
        return dummy.next; 
    } 
}
n# @lc code=end