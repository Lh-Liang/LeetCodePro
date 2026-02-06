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
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        ListNode curr = head;
        int groupSize = 1;
        while (curr != null) {
            int count = 0;
            ListNode groupStart = curr;
            ListNode temp = curr;
            // Find the actual size of the current group
            while (temp != null && count < groupSize) {
                temp = temp.next;
                count++;
            }
            ListNode groupEndNext = temp;
            // If the group has even length, reverse it
            if (count % 2 == 0) {
                ListNode prevNode = groupEndNext;
                ListNode node = groupStart;
                for (int i = 0; i < count; i++) {
                    ListNode nextNode = node.next;
                    node.next = prevNode;
                    prevNode = node;
                    node = nextNode;
                }
                prev.next = prevNode;
                prev = groupStart;
                curr = groupEndNext;
            } else {
                // No reversal, move prev and curr to the end of the group
                for (int i = 0; i < count; i++) {
                    prev = curr;
                    curr = curr.next;
                }
            }
            groupSize++;
        }
        return dummy.next;
    }
}
# @lc code=end