#
# @lc app=leetcode id=3530 lang=java
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
class Solution {
    public int maxProfit(int n, int[][] edges, int[] score) {
        // Build graph: adjacency list and indegree
        List<Integer>[] adj = new ArrayList[n];
        int[] indegree = new int[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            indegree[e[1]]++;
        }
        int N = 1 << n;
        int[] dp = new int[N];
        Arrays.fill(dp, Integer.MIN_VALUE);
        dp[0] = 0;
        // For each mask, try all available nodes
        for (int mask = 0; mask < N; ++mask) {
            if (dp[mask] == Integer.MIN_VALUE) continue;
            // Compute current indegrees for nodes not in mask
            int[] currIndeg = new int[n];
            for (int i = 0; i < n; ++i) currIndeg[i] = indegree[i];
            for (int i = 0; i < n; ++i) {
                if ((mask & (1<<i)) != 0) {
                    // Remove i from graph
                    for (int v : adj[i]) currIndeg[v]--;
                }
            }
            // For each node not in mask, if currIndeg==0, can pick
            for (int i = 0; i < n; ++i) {
                if ((mask & (1<<i)) == 0 && currIndeg[i] == 0) {
                    int newMask = mask | (1<<i);
                    int pos = Integer.bitCount(mask) + 1;
                    dp[newMask] = Math.max(dp[newMask], dp[mask] + score[i] * pos);
                }
            }
        }
        return dp[N-1];
    }
}
# @lc code=end