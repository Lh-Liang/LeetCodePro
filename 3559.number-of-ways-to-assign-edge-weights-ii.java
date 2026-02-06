#
# @lc app=leetcode id=3559 lang=java
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
import java.util.*;
class Solution {
    static final int MOD = 1000000007;
    int LOGN = 17; // since n <= 1e5, log2(1e5) < 17
    List<Integer>[] tree;
    int[][] parent;
    int[] depth;
    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        tree = new ArrayList[n + 1];
        for (int i = 1; i <= n; ++i) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }
        LOGN = 1;
        while ((1 << LOGN) <= n) LOGN++;
        parent = new int[n + 1][LOGN];
        depth = new int[n + 1];
        dfs(1, 0);
        for (int k = 1; k < LOGN; ++k)
            for (int v = 1; v <= n; ++v)
                parent[v][k] = parent[parent[v][k - 1]][k - 1];

        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            int u = queries[i][0], v = queries[i][1];
            int lca = findLCA(u, v);
            int k = depth[u] + depth[v] - 2 * depth[lca];
            if (k == 0) {
                answer[i] = 0;
            } else {
                answer[i] = powmod(2, k - 1, MOD);
            }
        }
        return answer;
    }
    void dfs(int u, int p) {
        parent[u][0] = p;
        for (int v : tree[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }
    int findLCA(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        for (int k = LOGN - 1; k >= 0; --k) {
            if (depth[u] - (1 << k) >= depth[v]) u = parent[u][k];
        }
        if (u == v) return u;
        for (int k = LOGN - 1; k >= 0; --k) {
            if (parent[u][k] != parent[v][k]) {
                u = parent[u][k];
                v = parent[v][k];
            }
        }
        return parent[u][0];
    }
    int powmod(int a, int b, int mod) {
        long res = 1, x = a;
        while (b > 0) {
            if ((b & 1) == 1) res = (res * x) % mod;
            x = (x * x) % mod;
            b >>= 1;
        }
        return (int) res;
    }
}
# @lc code=end