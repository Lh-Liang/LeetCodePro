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
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        // Step 1: Populate HashSet for quick look-up of nodes to delete.
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        // Step 2: Initialize dummy node and pointers.
        ListNode dummy = new ListNode(0); // Dummy node simplifies edge case handling.
        dummy.next = head;
        ListNode current = head;
        ListNode prev = dummy;
        
        // Step 3: Traverse and modify list based on presence in numSet.
        while (current != null) {
            if (numSet.contains(current.val)) {
                prev.next = current.next; // Remove current by linking prev to current's next.
            } else {
                prev = current; // Move prev forward only if no deletion occurs.
            }
            current = current.next; // Always move current forward.
        }
        
        // Step 4: Return new head of list after deletions are done.
        return dummy.next;
    }
}
# @lc code=end