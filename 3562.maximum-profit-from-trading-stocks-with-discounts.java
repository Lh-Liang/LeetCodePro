#
# @lc app=leetcode id=3562 lang=java
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
class Solution {
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        // Build tree structure
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] edge : hierarchy) {
            tree[edge[0] - 1].add(edge[1] - 1);
        }
        // dp[u][b][0]: max profit for node u in subtree, budget b, boss didn't buy
        // dp[u][b][1]: max profit for node u in subtree, budget b, boss did buy (discount)
        int[][][] dp = new int[n][budget + 1][2];
        dfs(0, tree, present, future, dp, budget);
        int ans = 0;
        for (int b = 0; b <= budget; ++b) {
            ans = Math.max(ans, Math.max(dp[0][b][0], dp[0][b][1]));
        }
        return ans;
    }

    private void dfs(int u, List<Integer>[] tree, int[] present, int[] future, int[][][] dp, int budget) {
        // Prepare DP for this node
        // Base cases: only self
        int cost0 = present[u];
        int profit0 = future[u] - present[u];
        int cost1 = present[u] / 2;
        int profit1 = future[u] - cost1;
        for (int b = 0; b <= budget; ++b) {
            dp[u][b][0] = 0;
            dp[u][b][1] = 0;
            if (b >= cost0) dp[u][b][0] = profit0;
            if (b >= cost1) dp[u][b][1] = profit1;
        }
        // Merge with children
        for (int v : tree[u]) {
            dfs(v, tree, present, future, dp, budget);
            int[][] ndp = new int[budget + 1][2];
            for (int b = 0; b <= budget; ++b) {
                ndp[b][0] = dp[u][b][0];
                ndp[b][1] = dp[u][b][1];
            }
            // Merge child v
            for (int b = budget; b >= 0; --b) {
                for (int cb = 0; cb <= b; ++cb) {
                    // If u not bought, v must use no-discount
                    ndp[b][0] = Math.max(ndp[b][0], dp[u][b - cb][0] + dp[v][cb][0]);
                    // If u bought, v can use discounted or non-discounted
                    ndp[b][1] = Math.max(ndp[b][1], dp[u][b - cb][1] + Math.max(dp[v][cb][0], dp[v][cb][1]));
                }
            }
            dp[u] = ndp;
        }
    }
}
# @lc code=end