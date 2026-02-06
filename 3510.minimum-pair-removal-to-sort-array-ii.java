#
# @lc app=leetcode id=3510 lang=java
#
# [3510] Minimum Pair Removal to Sort Array II
#
# @lc code=start
import java.util.*;
class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;
        boolean sorted = true;
        for (int i = 1; i < n; ++i) {
            if (nums[i] < nums[i-1]) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;
        // Doubly linked list node
        class Node {
            int val;
            Node prev, next;
            int idx;  // for leftmost tie-breaking
            Node(int val, int idx) { this.val = val; this.idx = idx; }
        }
        // Pair structure for heap: (sum, index, left node)
        class Pair implements Comparable<Pair> {
            int sum, idx;
            Node left;
            Pair(int sum, int idx, Node left) { this.sum = sum; this.idx = idx; this.left = left; }
            public int compareTo(Pair o) {
                if (this.sum != o.sum) return this.sum - o.sum;
                return this.idx - o.idx;  // leftmost tie-break
            }
        }
        // Build doubly linked list of nodes
        Node[] nodes = new Node[n];
        for (int i = 0; i < n; ++i) nodes[i] = new Node(nums[i], i);
        for (int i = 0; i < n; ++i) {
            if (i > 0) nodes[i].prev = nodes[i-1];
            if (i < n-1) nodes[i].next = nodes[i+1];
        }
        // Build initial heap of all adjacent pairs
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        Set<Node> alive = new HashSet<>(Arrays.asList(nodes));
        for (int i = 0; i < n-1; ++i) {
            pq.offer(new Pair(nodes[i].val + nodes[i+1].val, nodes[i].idx, nodes[i]));
        }
        int ops = 0;
        while (alive.size() > 1) {
            // Remove invalid pairs
            while (!pq.isEmpty() && (pq.peek().left.next == null || !alive.contains(pq.peek().left) || !alive.contains(pq.peek().left.next))) {
                pq.poll();
            }
            if (pq.isEmpty()) break;
            Pair p = pq.poll();
            Node l = p.left, r = l.next;
            // Merge l and r
            Node merged = new Node(l.val + r.val, l.idx);
            // Re-link
            Node pl = l.prev, nr = r.next;
            if (pl != null) { pl.next = merged; merged.prev = pl; }
            if (nr != null) { merged.next = nr; nr.prev = merged; }
            alive.remove(l); alive.remove(r); alive.add(merged);
            // Insert new adjacent pairs
            if (merged.prev != null)
                pq.offer(new Pair(merged.prev.val + merged.val, merged.prev.idx, merged.prev));
            if (merged.next != null)
                pq.offer(new Pair(merged.val + merged.next.val, merged.idx, merged));
            ops++;
            // Check if now non-decreasing
            boolean isSorted = true;
            Node cur = merged;
            while (cur.prev != null) cur = cur.prev;
            Node prev = null;
            while (cur != null) {
                if (prev != null && cur.val < prev.val) { isSorted = false; break; }
                prev = cur; cur = cur.next;
            }
            if (isSorted) break;
        }
        return ops;
    }
}
# @lc code=end