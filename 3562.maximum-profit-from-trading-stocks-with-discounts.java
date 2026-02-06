#
# @lc app=leetcode id=3562 lang=java
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
import java.util.*;
class Solution {
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        // Build adjacency list (1-based input, adjust to 0-based)
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] edge : hierarchy) {
            tree[edge[0] - 1].add(edge[1] - 1);
        }
        // DP function: returns int[2][budget+1]: dp0 (parent hasn't bought), dp1 (parent has bought)
        int[][] dfs(int node) {
            int[][] dp = new int[2][budget + 1];
            for (int[] arr : dp) Arrays.fill(arr, Integer.MIN_VALUE);
            // Two scenarios: parent bought or not
            // Case 0: parent didn't buy, so must pay full price
            for (int b = present[node]; b <= budget; ++b) {
                dp[0][b] = future[node] - present[node];
            }
            // Case 1: parent bought, can buy at floor(present[node]/2)
            int half = present[node] / 2;
            for (int b = half; b <= budget; ++b) {
                dp[1][b] = future[node] - half;
            }
            // Merge children
            for (int child : tree[node]) {
                int[][] childDP = dfs(child);
                int[][] ndp = new int[2][budget + 1];
                for (int t = 0; t < 2; ++t) {
                    Arrays.fill(ndp[t], Integer.MIN_VALUE);
                    for (int b = 0; b <= budget; ++b) {
                        if (dp[t][b] < 0) continue;
                        for (int cb = 0; cb <= b; ++cb) {
                            int val = dp[t][b - cb];
                            // If we buy current, child sees us as boss (gets discount)
                            if (childDP[1][cb] >= 0) ndp[t][b] = Math.max(ndp[t][b], val + childDP[1][cb]);
                            // Or, don't buy current, child doesn't get discount
                            if (childDP[0][cb] >= 0) ndp[t][b] = Math.max(ndp[t][b], val + childDP[0][cb]);
                        }
                    }
                }
                dp = ndp;
            }
            // Option to skip buying at this node: allow 0 profit if we don't buy
            for (int t = 0; t < 2; ++t) {
                for (int b = 0; b <= budget; ++b) {
                    dp[t][b] = Math.max(dp[t][b], 0);
                }
            }
            return dp;
        }
        int[][] res = dfs(0);
        int ans = 0;
        for (int t = 0; t < 2; ++t) {
            for (int b = 0; b <= budget; ++b) {
                ans = Math.max(ans, res[t][b]);
            }
        }
        return ans;
    }
}
# @lc code=end