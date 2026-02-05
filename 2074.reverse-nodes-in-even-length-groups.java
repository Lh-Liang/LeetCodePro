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
            // Step 2: Identify group boundaries
            int cnt = 0;
            ListNode groupStart = curr;
            ListNode temp = curr;
            while (cnt < groupSize && temp != null) {
                temp = temp.next;
                cnt++;
            }
            // Step 3: Handle last group (less than expected size)
            // Step 4: Reverse if even size
            if (cnt % 2 == 0) {
                // (a) Store node after group for reconnection
                ListNode nextGroup = temp;
                // (b) Reverse current group
                ListNode prevNode = nextGroup;
                ListNode node = curr;
                for (int i = 0; i < cnt; i++) {
                    ListNode nextNode = node.next;
                    node.next = prevNode;
                    prevNode = node;
                    node = nextNode;
                }
                // (c) Reconnect reversed group
                prev.next = prevNode;
                prev = curr;
                curr = temp;
            } else {
                // If odd, advance pointers
                for (int i = 0; i < cnt; i++) {
                    prev = curr;
                    curr = curr.next;
                }
            }
            // Step 5: Verification (implicit in pointer updates)
            groupSize++;
        }
        return dummy.next;
    }
}
# @lc code=end