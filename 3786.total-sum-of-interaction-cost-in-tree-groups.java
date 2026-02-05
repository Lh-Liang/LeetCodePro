#
# @lc app=leetcode id=3786 lang=java
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
import java.util.*;
class Solution {
    public long interactionCosts(int n, int[][] edges, int[] group) {
        // Step 1: Build adjacency list
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }
        // Step 2: Group nodes by label
        Map<Integer, List<Integer>> groupMap = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            groupMap.computeIfAbsent(group[i], k -> new ArrayList<>()).add(i);
        }
        long total = 0;
        // Step 3: For each group, compute interaction cost
        for (Map.Entry<Integer, List<Integer>> entry : groupMap.entrySet()) {
            Set<Integer> members = new HashSet<>(entry.getValue());
            if (members.size() <= 1) continue; // only pairs
            int[] count = new int[n];
            // DFS to count group members in subtree
            dfsCount(0, -1, tree, members, count);
            // For each edge, sum contributions, only once per edge (u < v)
            for (int u = 0; u < n; ++u) {
                for (int v : tree[u]) {
                    if (u < v) {
                        int cu = count[u] < count[v] ? count[u] : count[v];
                        int cv = members.size() - cu;
                        total += (long)cu * cv;
                    }
                }
            }
        }
        // Step 5: (Verification) Optionally, verify that each pair is counted exactly once
        return total;
    }
    // Helper DFS: returns count of group members in subtree rooted at node
    private int dfsCount(int node, int parent, List<Integer>[] tree, Set<Integer> members, int[] count) {
        count[node] = members.contains(node) ? 1 : 0;
        for (int nei : tree[node]) {
            if (nei == parent) continue;
            count[node] += dfsCount(nei, node, tree, members, count);
        }
        return count[node];
    }
}
# @lc code=end