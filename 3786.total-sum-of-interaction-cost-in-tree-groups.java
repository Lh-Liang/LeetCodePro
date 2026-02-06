#
# @lc app=leetcode id=3786 lang=java
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution {
    public long interactionCosts(int n, int[][] edges, int[] group) {
        // Build the tree
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }

        // Map group id to nodes
        Map<Integer, List<Integer>> groupMap = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            groupMap.computeIfAbsent(group[i], k -> new ArrayList<>()).add(i);
        }

        long total = 0;
        for (int gid : groupMap.keySet()) {
            List<Integer> nodes = groupMap.get(gid);
            if (nodes.size() < 2) continue;
            boolean[] inGroup = new boolean[n];
            for (int x : nodes) inGroup[x] = true;
            int totalInGroup = nodes.size();

            // DFS to compute subtree sizes for current group
            int[] subtree = new int[n];
            dfs(0, -1, tree, inGroup, subtree);

            // For each edge, calculate contribution
            for (int[] e : edges) {
                int u = e[0], v = e[1];
                // Find parent-child (need to determine direction)
                // We'll use subtree sizes to infer direction
                // If subtree[v] < subtree[u], swap
                if (subtree[v] > subtree[u]) { int tmp = u; u = v; v = tmp; }
                // Now u is parent of v
                int count = subtree[v];
                total += (long) count * (totalInGroup - count);
            }
        }
        return total;
    }

    // Returns how many nodes in this subtree belong to group
    private int dfs(int node, int parent, List<Integer>[] tree, boolean[] inGroup, int[] subtree) {
        int cnt = inGroup[node] ? 1 : 0;
        for (int nei : tree[node]) {
            if (nei == parent) continue;
            cnt += dfs(nei, node, tree, inGroup, subtree);
        }
        return subtree[node] = cnt;
    }
}
# @lc code=end