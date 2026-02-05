#
# @lc app=leetcode id=3510 lang=java
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
import java.util.*;
class Solution {
    private static class Node {
        int val;
        Node prev, next;
        int idx;
        Node(int val, int idx) { this.val = val; this.idx = idx; }
    }
    private static class Pair implements Comparable<Pair> {
        Node left, right;
        int sum, idx;
        Pair(Node left, Node right) {
            this.left = left; this.right = right;
            this.sum = left.val + right.val; this.idx = left.idx;
        }
        public int compareTo(Pair o) {
            if (this.sum != o.sum) return Integer.compare(this.sum, o.sum);
            return Integer.compare(this.idx, o.idx);
        }
    }
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;
        boolean sorted = true;
        for (int i = 1; i < n; ++i) if (nums[i-1] > nums[i]) { sorted = false; break; }
        if (sorted) return 0;
        List<Node> nodes = new ArrayList<>();
        for (int i = 0; i < n; ++i) nodes.add(new Node(nums[i], i));
        for (int i = 0; i < n - 1; ++i) {
            nodes.get(i).next = nodes.get(i + 1);
            nodes.get(i + 1).prev = nodes.get(i);
        }
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        for (int i = 0; i < n - 1; ++i) {
            pq.offer(new Pair(nodes.get(i), nodes.get(i + 1)));
        }
        Set<Node> removed = new HashSet<>();
        int ops = 0;
        while (true) {
            // Explicit verification step
            Node curr = nodes.get(0);
            sorted = true;
            while (curr.next != null) {
                if (curr.val > curr.next.val) { sorted = false; break; }
                curr = curr.next;
            }
            if (sorted) break;
            while (!pq.isEmpty()) {
                Pair p = pq.poll();
                if (removed.contains(p.left) || removed.contains(p.right) || p.left.next != p.right) continue;
                // Merge p.left and p.right
                Node merged = new Node(p.left.val + p.right.val, p.left.idx);
                removed.add(p.left); removed.add(p.right);
                Node l = p.left.prev, r = p.right.next;
                if (l != null) { l.next = merged; merged.prev = l; }
                if (r != null) { r.prev = merged; merged.next = r; }
                if (l == null) nodes.set(0, merged);
                ops++;
                // Update affected pairs
                if (merged.prev != null) pq.offer(new Pair(merged.prev, merged));
                if (merged.next != null) pq.offer(new Pair(merged, merged.next));
                break;
            }
        }
        return ops;
    }
}
# @lc code=end