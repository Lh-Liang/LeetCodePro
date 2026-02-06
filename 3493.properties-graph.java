#
# @lc app=leetcode id=3493 lang=java
#
# [3493] Properties Graph
#
# @lc code=start
class Solution {
    public int numberOfComponents(int[][] properties, int k) {
        int n = properties.length;
        List<Integer>[] adj = new List[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        // Build adjacency list
        for (int i = 0; i < n; i++) {
            Set<Integer> setI = new HashSet<>();
            for (int val : properties[i]) setI.add(val);
            for (int j = i + 1; j < n; j++) {
                Set<Integer> setJ = new HashSet<>();
                for (int val : properties[j]) setJ.add(val);
                Set<Integer> intersection = new HashSet<>(setI);
                intersection.retainAll(setJ);
                if (intersection.size() >= k) {
                    adj[i].add(j);
                    adj[j].add(i);
                }
            }
        }
        boolean[] visited = new boolean[n];
        int components = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                components++;
                dfs(i, adj, visited);
            }
        }
        return components;
    }
    private void dfs(int node, List<Integer>[] adj, boolean[] visited) {
        visited[node] = true;
        for (int nei : adj[node]) {
            if (!visited[nei]) dfs(nei, adj, visited);
        }
    }
}
# @lc code=end