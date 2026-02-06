#
# @lc app=leetcode id=3553 lang=java
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#
# @lc code=start
import java.util.*;
class Solution {
    int LOG = 17; // since n <= 1e5, log2(1e5) ~ 17
    int n;
    List<int[]>[] tree;
    int[] depth, parent, tin, tout;
    int[][] up;
    long[] weightSum;
    int timer = 0;
    void dfs(int u, int p, int d, long w) {
        depth[u] = d;
        tin[u] = timer++;
        parent[u] = p;
        weightSum[u] = w;
        up[u][0] = p == -1 ? u : p;
        for (int i = 1; i < LOG; ++i) {
            up[u][i] = up[up[u][i-1]][i-1];
        }
        for (int[] nei : tree[u]) {
            int v = nei[0], wt = nei[1];
            if (v != p) {
                dfs(v, u, d+1, w + wt);
            }
        }
        tout[u] = timer++;
    }
    boolean isAncestor(int u, int v) {
        return tin[u] <= tin[v] && tout[u] >= tout[v];
    }
    int lca(int u, int v) {
        if (isAncestor(u, v)) return u;
        if (isAncestor(v, u)) return v;
        for (int i = LOG - 1; i >= 0; --i) {
            if (!isAncestor(up[u][i], v)) {
                u = up[u][i];
            }
        }
        return up[u][0];
    }
    public int[] minimumWeight(int[][] edges, int[][] queries) {
        n = edges.length + 1;
        tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            tree[u].add(new int[]{v, w});
            tree[v].add(new int[]{u, w});
        }
        depth = new int[n];
        parent = new int[n];
        tin = new int[n];
        tout = new int[n];
        up = new int[n][LOG];
        weightSum = new long[n];
        dfs(0, -1, 0, 0L);
        int q = queries.length;
        int[] res = new int[q];
        for (int i = 0; i < q; ++i) {
            int a = queries[i][0], b = queries[i][1], c = queries[i][2];
            int l1 = lca(a, c);
            int l2 = lca(b, c);
            int l3 = lca(a, b);
            // The union of paths from a to c and b to c is: sum(a to c) + sum(b to c) - sum(lca(a, b) to c)
            long ans = weightSum[a] + weightSum[b] - weightSum[l3] + weightSum[c] - weightSum[l1] - weightSum[l2] + weightSum[lca(l1, l2)];
            res[i] = (int) ans;
        }
        return res;
    }
}
# @lc code=end