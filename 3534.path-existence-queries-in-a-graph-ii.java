#
# @lc app=leetcode id=3534 lang=java
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
import java.util.*;
class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        // Step 1: Sort nodes by nums and connect via Union-Find
        int[] idx = new int[n];
        for (int i = 0; i < n; ++i) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(nums[a], nums[b]));
        DSU dsu = new DSU(n);
        for (int i = 1; i < n; ++i) {
            if (Math.abs(nums[idx[i]] - nums[idx[i-1]]) <= maxDiff) {
                dsu.union(idx[i], idx[i-1]);
            }
        }
        // Step 2: Build adjacency list for connected nodes within maxDiff
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) {
            if (Math.abs(nums[idx[i]] - nums[idx[i-1]]) <= maxDiff) {
                adj[idx[i]].add(idx[i-1]);
                adj[idx[i-1]].add(idx[i]);
            }
        }
        // Step 3: For each unique source in queries, run BFS in its component
        Map<Integer, Set<Integer>> compToSources = new HashMap<>();
        for (int[] q : queries) {
            int root = dsu.find(q[0]);
            compToSources.computeIfAbsent(root, k -> new HashSet<>()).add(q[0]);
        }
        // For each (component, source), run BFS and store distances
        Map<Integer, Map<Integer, Map<Integer, Integer>>> compToSourceDist = new HashMap<>();
        for (Map.Entry<Integer, Set<Integer>> entry : compToSources.entrySet()) {
            int comp = entry.getKey();
            Set<Integer> sources = entry.getValue();
            // collect all nodes in this component
            List<Integer> componentNodes = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                if (dsu.find(i) == comp) componentNodes.add(i);
            }
            Map<Integer, Map<Integer, Integer>> sourceDist = new HashMap<>();
            for (int source : sources) {
                Map<Integer, Integer> dist = new HashMap<>();
                Queue<Integer> queue = new LinkedList<>();
                dist.put(source, 0);
                queue.offer(source);
                while (!queue.isEmpty()) {
                    int u = queue.poll();
                    for (int v : adj[u]) {
                        if (!dist.containsKey(v)) {
                            dist.put(v, dist.get(u) + 1);
                            queue.offer(v);
                        }
                    }
                }
                sourceDist.put(source, dist);
            }
            compToSourceDist.put(comp, sourceDist);
        }
        // Step 4: Answer queries
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                ans[i] = 0;
                continue;
            }
            if (dsu.find(u) != dsu.find(v)) {
                ans[i] = -1;
                continue;
            }
            Map<Integer, Integer> distMap = compToSourceDist.get(dsu.find(u)).get(u);
            ans[i] = distMap.getOrDefault(v, -1);
        }
        return ans;
    }
    static class DSU {
        int[] parent, rank;
        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; ++i) parent[i] = i;
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void union(int x, int y) {
            int xr = find(x), yr = find(y);
            if (xr == yr) return;
            if (rank[xr] < rank[yr]) parent[xr] = yr;
            else if (rank[xr] > rank[yr]) parent[yr] = xr;
            else { parent[yr] = xr; rank[xr]++; }
        }
    }
}
# @lc code=end