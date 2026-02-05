# @lc app=leetcode id=2058 lang=java
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int firstCritical = -1;
        int prevCritical = -1;
        int minDistance = Integer.MAX_VALUE;
        int index = 0;
        List<Integer> criticalPoints = new ArrayList<>();

        ListNode prev = null;
        ListNode current = head;

        while (current != null && current.next != null) {
            if (prev != null && (current.val > prev.val && current.val > current.next.val ||
                                 current.val < prev.val && current.val < current.next.val)) {
                if (firstCritical == -1) {
                    firstCritical = index;
                } else {
                    minDistance = Math.min(minDistance, index - prevCritical);
                }
                prevCritical = index;
                criticalPoints.add(index);
            }
            prev = current;
            current = current.next;
            index++;
        }

        if (criticalPoints.size() < 2) {
            return new int[]{-1, -1};
        }

        int maxDistance = criticalPoints.get(criticalPoints.size() - 1) - firstCritical;

        return new int[]{minDistance, maxDistance};
    }
}
# @lc code=end