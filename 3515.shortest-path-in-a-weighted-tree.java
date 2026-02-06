#
# @lc app=leetcode id=3515 lang=java
#
# [3515] Shortest Path in a Weighted Tree
#
# @lc code=start
import java.util.*;
class Solution {
    public int[] treeQueries(int n, int[][] edges, int[][] queries) {
        // Build adjacency list and map edge (min(u,v), max(u,v)) to edge index
        List<int[]>[] tree = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) tree[i] = new ArrayList<>();
        Map<Long, Integer> edgeIndex = new HashMap<>();
        int edgeId = 0;
        for (int[] e : edges) {
            tree[e[0]].add(new int[]{e[1], e[2], edgeId});
            tree[e[1]].add(new int[]{e[0], e[2], edgeId});
            long key = ((long)Math.min(e[0],e[1]) << 32) | Math.max(e[0],e[1]);
            edgeIndex.put(key, edgeId++);
        }
        // Euler tour, parent, depth, dfs order
        int[] in = new int[n+1], out = new int[n+1];
        int[] parent = new int[n+1], edgeToParent = new int[n+1];
        long[] dist = new long[n+1];
        int time = 0;
        int[] order = new int[n+1];
        int[] edgeWeights = new int[n];
        Arrays.fill(edgeToParent, -1);
        dfs(1, 0, 0, tree, in, out, parent, edgeToParent, dist, order, edgeWeights, time);
        // Build Fenwick tree / BIT
        FenwickTree bit = new FenwickTree(n+2);
        for (int i = 1; i <= n; i++) {
            bit.add(in[i], dist[i]);
            bit.add(out[i], -dist[i]);
        }
        int[] res = new int[(int)Arrays.stream(queries).filter(q->q[0]==2).count()];
        int idx = 0;
        int[] eidToNode = new int[n]; // eid->child node
        for (int i = 2; i <= n; i++) eidToNode[edgeToParent[i]] = i;
        for (int[] q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], w = q[3];
                long key = ((long)Math.min(u,v)<<32)|Math.max(u,v);
                int eid = edgeIndex.get(key);
                int node = eidToNode[eid];
                int oldw = edgeWeights[eid];
                int delta = w - oldw;
                edgeWeights[eid] = w;
                bit.add(in[node], delta);
                bit.add(out[node], -delta);
            } else {
                int x = q[1];
                res[idx++] = (int)bit.query(in[x]);
            }
        }
        return res;
    }
    void dfs(int u, int p, long d, List<int[]>[] tree, int[] in, int[] out, int[] parent, int[] edgeToParent, long[] dist, int[] order, int[] edgeWeights, int time) {
        in[u] = ++time;
        dist[u] = d;
        parent[u] = p;
        for (int[] nei : tree[u]) {
            int v = nei[0], w = nei[1], eid = nei[2];
            if (v == p) continue;
            edgeToParent[v] = eid;
            edgeWeights[eid] = w;
            dfs(v, u, d + w, tree, in, out, parent, edgeToParent, dist, order, edgeWeights, time);
        }
        out[u] = ++time;
    }
    static class FenwickTree {
        long[] tree; int n;
        FenwickTree(int n) { this.n = n; tree = new long[n+2]; }
        void add(int i, long v) { for (; i < tree.length; i += i&-i) tree[i] += v; }
        long query(int i) { long s = 0; for (; i > 0; i -= i&-i) s += tree[i]; return s; }
    }
}
# @lc code=end