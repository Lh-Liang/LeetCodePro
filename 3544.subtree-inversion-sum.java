#
# @lc app=leetcode id=3544 lang=java
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
class Solution {
    public long subtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = nums.length;
        List<Integer>[] tree = new List[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }
        // dp[u][d]: max sum for node u with distance d from last inversion
        long[][] dp = new long[n][k+2];
        boolean[][] visited = new boolean[n][k+2];
        return dfs(0, -1, k+1, tree, nums, k, dp, visited);
    }
    private long dfs(int u, int parent, int dist, List<Integer>[] tree, int[] nums, int k, long[][] dp, boolean[][] visited) {
        if (visited[u][dist]) return dp[u][dist];
        visited[u][dist] = true;
        // Case 1: Do not invert at u
        long sum1 = nums[u];
        for (int v : tree[u]) {
            if (v == parent) continue;
            sum1 += dfs(v, u, Math.min(dist+1, k+1), tree, nums, k, dp, visited);
        }
        long res = sum1;
        // Case 2: Invert at u, if allowed
        if (dist >= k) {
            long sum2 = -nums[u];
            for (int v : tree[u]) {
                if (v == parent) continue;
                sum2 += dfs(v, u, 1, tree, nums, k, dp, visited);
            }
            res = Math.max(res, sum2);
        }
        dp[u][dist] = res;
        return res;
    }
}
# @lc code=end