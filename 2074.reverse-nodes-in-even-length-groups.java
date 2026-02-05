#
# @lc app=leetcode id=2074 lang=java
#
# [2074] Reverse Nodes in Even Length Groups
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
    public ListNode reverseEvenLengthGroups(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int groupLen = 1;
        while (prev.next != null) {
            // Find the size of current group
            ListNode start = prev.next;
            int count = 0;
            ListNode end = prev;
            while (count < groupLen && end.next != null) {
                end = end.next;
                count++;
            }
            // Reverse nodes if count is even
            if (count % 2 == 0) {
                prev.next = reverse(start, count);
                start.next = end.next; // Connect last reversed node to rest of list
                prev = start; // Move prev to last node in reversed section
            } else {
                prev = end; // Move prev to last node in current section without reversal
            }
            groupLen++;
        }
        return dummy.next;
    }
    
    private ListNode reverse(ListNode head, int k) {
        ListNode prev = null, curr = head, next = null;
        while (k-- > 0 && curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev; // New head after reversal
    }
}
dummy// @lc code=end