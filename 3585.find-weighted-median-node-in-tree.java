#
# @lc app=leetcode id=3585 lang=java
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
import java.util.*;
class Solution {
    static class Edge {
        int to, w;
        Edge(int to, int w) { this.to = to; this.w = w; }
    }
    int LOG;
    int[] depth, parent, sumWeight;
    int[][] up;
    int[] upWeight;
    List<Edge>[] tree;
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        tree = new ArrayList[n];
        for (int i = 0; i < n; i++) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(new Edge(e[1], e[2]));
            tree[e[1]].add(new Edge(e[0], e[2]));
        }
        LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        depth = new int[n];
        parent = new int[n];
        sumWeight = new int[n];
        up = new int[n][LOG];
        upWeight = new int[n];
        dfs(0, -1, 0, 0);
        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                if (up[v][k - 1] != -1) {
                    up[v][k] = up[up[v][k - 1]][k - 1];
                } else {
                    up[v][k] = -1;
                }
            }
        }
        int[] res = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int u = queries[qi][0], v = queries[qi][1];
            int lca = getLCA(u, v);
            int total = sumWeight[u] + sumWeight[v] - 2 * sumWeight[lca];
            int half = (total % 2 == 0) ? total / 2 : total / 2 + 1;
            // Walk from u to v, accumulate weights, find first node >= half
            int node = u, dist = 0;
            if (u == v) { res[qi] = u; continue; }
            // Step 1: try going up from u towards lca
            int curr = u;
            int currW = 0;
            while (curr != lca) {
                int par = parent[curr];
                int w = sumWeight[curr] - sumWeight[par];
                currW += w;
                if (currW >= half) {
                    res[qi] = curr;
                    break;
                }
                curr = par;
            }
            if (currW >= half) continue;
            // Step 2: go from lca down to v
            // build path from lca to v
            List<Integer> path = new ArrayList<>();
            curr = v;
            while (curr != lca) {
                path.add(curr);
                curr = parent[curr];
            }
            Collections.reverse(path);
            for (int x : path) {
                int par = parent[x];
                int w = sumWeight[x] - sumWeight[par];
                currW += w;
                if (currW >= half) {
                    res[qi] = x;
                    break;
                }
            }
        }
        return res;
    }
    void dfs(int v, int p, int d, int wsum) {
        parent[v] = (p == -1 ? v : p);
        depth[v] = d;
        sumWeight[v] = wsum;
        up[v][0] = (p == -1 ? -1 : p);
        for (Edge e : tree[v]) {
            if (e.to != p) {
                dfs(e.to, v, d + 1, wsum + e.w);
            }
        }
    }
    int getLCA(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[u][k] != -1 && depth[up[u][k]] >= depth[v]) {
                u = up[u][k];
            }
        }
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[u][k] != -1 && up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }
        return parent[u];
    }
}
# @lc code=end