#
# @lc app=leetcode id=3559 lang=java
#
# [3559] Number of Ways to Assign Edge Weights II
#
# @lc code=start
class Solution {
    static final int MOD = 1000000007;
    int[][] up;
    int[] depth;
    int LOG;
    List<Integer>[] tree;
    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        tree = new List[n + 1];
        for (int i = 1; i <= n; i++) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
            tree[e[1]].add(e[0]);
        }
        up = new int[n + 1][LOG];
        depth = new int[n + 1];
        dfs(1, 1);
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], v = queries[i][1];
            int k = getDist(u, v);
            if (k == 0) {
                res[i] = 0;
            } else {
                res[i] = pow2(k - 1, MOD);
            }
        }
        return res;
    }
    void dfs(int u, int p) {
        up[u][0] = p;
        for (int i = 1; i < LOG; i++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
        for (int v : tree[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }
    int lca(int u, int v) {
        if (depth[u] < depth[v]) {
            int t = u; u = v; v = t;
        }
        for (int i = LOG - 1; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) {
                u = up[u][i];
            }
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }
    int getDist(int u, int v) {
        int a = lca(u, v);
        return depth[u] + depth[v] - 2 * depth[a];
    }
    int pow2(int k, int mod) {
        long res = 1, base = 2;
        while (k > 0) {
            if ((k & 1) != 0) res = (res * base) % mod;
            base = (base * base) % mod;
            k >>= 1;
        }
        return (int) res;
    }
}
# @lc code=end