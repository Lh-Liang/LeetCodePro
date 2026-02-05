class Solution {
    int N, LOG;
    List<int[]>[] tree;
    int[][] parent;
    int[][] upSum;
    int[] depth;

    public int[] minimumWeight(int[][] edges, int[][] queries) {
        N = edges.length + 1;
        LOG = 1;
        while ((1 << LOG) <= N) LOG++;
        tree = new ArrayList[N];
        for (int i = 0; i < N; i++) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(new int[]{e[1], e[2]});
            tree[e[1]].add(new int[]{e[0], e[2]});
        }
        parent = new int[N][LOG];
        upSum = new int[N][LOG];
        depth = new int[N];
        dfs(0, -1, 0, 0);
        for (int k = 1; k < LOG; k++) {
            for (int i = 0; i < N; i++) {
                if (parent[i][k-1] != -1) {
                    parent[i][k] = parent[parent[i][k-1]][k-1];
                    upSum[i][k] = upSum[i][k-1] + upSum[parent[i][k-1]][k-1];
                } else {
                    parent[i][k] = -1;
                }
            }
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int src1 = queries[i][0], src2 = queries[i][1], dest = queries[i][2];
            int l1 = lca(src1, dest);
            int l2 = lca(src2, dest);
            int l3 = lca(src1, src2);
            // Find the LCA of all three nodes to account for overlap.
            int l = lca(l1, src2);
            // Inclusion-exclusion: total weight is sum of paths from each to l, with overlaps counted once.
            int total = dist(src1, l) + dist(src2, l) + dist(dest, l);
            ans[i] = total;
        }
        return ans;
    }

    void dfs(int u, int p, int d, int w) {
        parent[u][0] = p;
        upSum[u][0] = w;
        depth[u] = d;
        for (int[] nei : tree[u]) {
            if (nei[0] != p) {
                dfs(nei[0], u, d + 1, nei[1]);
            }
        }
    }

    int lca(int u, int v) {
        if (depth[u] < depth[v]) { int tmp = u; u = v; v = tmp; }
        for (int k = LOG - 1; k >= 0; k--) {
            if (parent[u][k] != -1 && depth[parent[u][k]] >= depth[v]) {
                u = parent[u][k];
            }
        }
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) {
            if (parent[u][k] != -1 && parent[u][k] != parent[v][k]) {
                u = parent[u][k];
                v = parent[v][k];
            }
        }
        return parent[u][0];
    }

    int dist(int u, int v) {
        int ret = 0;
        if (depth[u] < depth[v]) { int tmp = u; u = v; v = tmp; }
        for (int k = LOG - 1; k >= 0; k--) {
            if (parent[u][k] != -1 && depth[parent[u][k]] >= depth[v]) {
                ret += upSum[u][k];
                u = parent[u][k];
            }
        }
        if (u == v) return ret;
        for (int k = LOG - 1; k >= 0; k--) {
            if (parent[u][k] != -1 && parent[u][k] != parent[v][k]) {
                ret += upSum[u][k] + upSum[v][k];
                u = parent[u][k];
                v = parent[v][k];
            }
        }
        return ret + upSum[u][0] + upSum[v][0];
    }
}