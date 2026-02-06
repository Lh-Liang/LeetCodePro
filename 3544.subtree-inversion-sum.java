#
# @lc app=leetcode id=3544 lang=java
#
# [3544] Subtree Inversion Sum
#
# @lc code=start
import java.util.*;
class Solution {
    public long subtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = nums.length;
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }
        // dp[u][d]: max sum for subtree rooted at u, d is distance to last inverted ancestor
        Long[][] dp = new Long[n][k+2];
        return dfs(0, -1, k, tree, nums, k, dp);
    }
    private long dfs(int u, int parent, int dist, List<Integer>[] tree, int[] nums, int k, Long[][] dp) {
        if (dp[u][dist] != null) return dp[u][dist];
        // Case 1: do not invert at u
        long sumNoInvert = nums[u];
        for (int v : tree[u]) {
            if (v == parent) continue;
            sumNoInvert += dfs(v, u, Math.min(dist+1, k+1), tree, nums, k, dp);
        }
        long res = sumNoInvert;
        // Case 2: invert at u (only if dist >= k)
        if (dist >= k) {
            long sumInvert = -nums[u];
            for (int v : tree[u]) {
                if (v == parent) continue;
                sumInvert += dfs(v, u, 1, tree, nums, k, dp);
            }
            res = Math.max(res, sumInvert);
        }
        return dp[u][dist] = res;
    }
}
# @lc code=end