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
        List<Integer> criticalIndices = new ArrayList<>();
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = head != null ? head.next : null;
        int pos = 1;
        while (next != null) {
            pos++;
            if (prev != null) {
                if ((curr.val > prev.val && curr.val > next.val) || (curr.val < prev.val && curr.val < next.val)) {
                    criticalIndices.add(pos - 1);
                }
            }
            prev = curr;
            curr = next;
            next = next.next;
        }
        if (criticalIndices.size() < 2) {
            return new int[]{-1, -1};
        }
        int minDist = Integer.MAX_VALUE;
        for (int i = 1; i < criticalIndices.size(); i++) {
            minDist = Math.min(minDist, criticalIndices.get(i) - criticalIndices.get(i - 1));
        }
        int maxDist = criticalIndices.get(criticalIndices.size() - 1) - criticalIndices.get(0);
        return new int[]{minDist, maxDist};
    }
}