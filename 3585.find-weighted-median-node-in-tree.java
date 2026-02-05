#
# @lc app=leetcode id=3585 lang=java
#
# [3585] Find Weighted Median Node in Tree
#
# @lc code=start
import java.util.*;
class Solution {
    static class Edge {
        int to, weight;
        Edge(int t, int w) { to = t; weight = w; }
    }
    int LOGN = 18; // since n <= 1e5, log2(1e5) ~ 17
    List<Edge>[] adj;
    int[][] up;
    int[] depth, parent;
    long[] dist; // prefix sum of weights from root
    int n;
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        this.n = n;
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new Edge(e[1], e[2]));
            adj[e[1]].add(new Edge(e[0], e[2]));
        }
        parent = new int[n];
        depth = new int[n];
        dist = new long[n];
        up = new int[n][LOGN];
        Arrays.fill(parent, -1);
        dfs(0, -1, 0, 0L);
        buildLCA();
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) { // edge case: same node
                ans[i] = u;
                continue;
            }
            int lca = getLCA(u, v);
            long total = dist[u] + dist[v] - 2 * dist[lca];
            long half = (total + 1) / 2; // need >= half, so round up
            int median = findWeightedMedian(u, v, lca, half, total);
            ans[i] = median;
        }
        return ans;
    }
    void dfs(int u, int p, int d, long sum) {
        parent[u] = p; depth[u] = d; dist[u] = sum;
        up[u][0] = p == -1 ? 0 : p;
        for (Edge e : adj[u]) {
            if (e.to == p) continue;
            dfs(e.to, u, d + 1, sum + e.weight);
        }
    }
    void buildLCA() {
        for (int k = 1; k < LOGN; k++) {
            for (int v = 0; v < n; v++) {
                up[v][k] = up[up[v][k - 1]][k - 1];
            }
        }
    }
    int getLCA(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        for (int k = LOGN - 1; k >= 0; k--) {
            if (depth[u] - (1 << k) >= depth[v]) u = up[u][k];
        }
        if (u == v) return u;
        for (int k = LOGN - 1; k >= 0; k--) {
            if (up[u][k] != up[v][k]) {
                u = up[u][k]; v = up[v][k];
            }
        }
        return parent[u];
    }
    int findWeightedMedian(int u, int v, int lca, long half, long total) {
        // Construct path from u to lca (excluding lca), then lca to v (excluding lca), so the full path is uj -> ... -> lca -> ... -> vj
        ArrayList<Integer> path = new ArrayList<>();
        int x = u;
        while (x != lca) {
            path.add(x);
            x = parent[x];
        }
        ArrayList<Integer> second = new ArrayList<>();
        x = v;
        while (x != lca) {
            second.add(x);
            x = parent[x];
        }
        path.add(lca);
        for (int i = second.size() - 1; i >= 0; i--) path.add(second.get(i));
        // Accumulate edge weights along the path
        long sum = 0;
        for (int i = 1; i < path.size(); i++) { // path[0] is uj
            int curr = path.get(i), prev = path.get(i - 1);
            long w = Math.abs(dist[curr] - dist[prev]);
            sum += w;
            if (sum >= half) {
                // Verification: ensure this is the first node with sum >= half
                return curr;
            }
        }
        // If not found in the loop, the weighted median is the last node (shouldn't happen in valid inputs)
        return path.get(path.size() - 1);
    }
}
# @lc code=end