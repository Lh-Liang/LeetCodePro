#
# @lc app=leetcode id=3530 lang=java
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
class Solution {
    public int maxProfit(int n, int[][] edges, int[] score) {
        int[] indegree = new int[n];
        List<Integer>[] adj = new List[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            indegree[e[1]]++;
        }
        // Prerequisite mask for each node
        int[] pre = new int[n];
        for (int u = 0; u < n; ++u) {
            for (int v : adj[u]) pre[v] |= (1 << u);
        }
        int size = 1 << n;
        int[] dp = new int[size];
        Arrays.fill(dp, Integer.MIN_VALUE);
        dp[0] = 0;
        for (int mask = 0; mask < size; ++mask) {
            int pos = Integer.bitCount(mask);
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) == 0 && (mask & pre[i]) == pre[i]) {
                    int next = mask | (1 << i);
                    dp[next] = Math.max(dp[next], dp[mask] + score[i] * (pos + 1));
                }
            }
        }
        return dp[size - 1];
    }
}
# @lc code=end