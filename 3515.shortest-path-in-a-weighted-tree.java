#
# @lc app=leetcode id=3515 lang=java
#
# [3515] Shortest Path in a Weighted Tree
#
# @lc code=start
class Solution {
    public int[] treeQueries(int n, int[][] edges, int[][] queries) {
        // Step 1: Build the tree and map each edge for efficient updates
        List<int[]>[] tree = new ArrayList[n + 1];
        for (int i = 1; i <= n; ++i) tree[i] = new ArrayList<>();
        Map<Long, Integer> edgeWeight = new HashMap<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            tree[u].add(new int[]{v, w});
            tree[v].add(new int[]{u, w});
            long key = key(u, v);
            edgeWeight.put(key, w);
        }
        // Step 2: DFS to assign parent, depth, and root distance
        int[] parent = new int[n + 1];
        int[] depth = new int[n + 1];
        long[] dist = new long[n + 1];
        dfs(1, 0, 0, 0, tree, parent, depth, dist);
        // Step 3: Flatten the tree (Euler Tour)
        int[] tin = new int[n + 1], tout = new int[n + 1];
        int[] nodeAt = new int[n + 1];
        int[] time = new int[]{1};
        flatten(1, 0, tree, tin, tout, nodeAt, time);
        long[] bit = new long[n + 2]; // Binary Indexed Tree for subtree updates
        List<Integer> answer = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], nw = q[3];
                long k = key(u, v);
                int oldw = edgeWeight.get(k);
                edgeWeight.put(k, nw);
                // Step 4: Determine child for the edge update (verify for correctness)
                int child;
                if (parent[u] == v) child = u;
                else if (parent[v] == u) child = v;
                else throw new IllegalStateException("Edge does not connect parent and child correctly");
                int delta = nw - oldw;
                update(bit, tin[child], tout[child], delta);
                // Optional: verification step (for debugging, can be omitted in production)
                // assert edgeWeight.get(k) == nw;
            } else {
                int x = q[1];
                // Step 5: Query the updated distance
                long d = dist[x] + query(bit, tin[x]);
                answer.add((int)d);
            }
        }
        // Step 6: Ensure answer array is aligned to queries
        int[] ans = new int[answer.size()];
        for (int i = 0; i < ans.length; ++i) ans[i] = answer.get(i);
        return ans;
    }
    private void dfs(int u, int p, int d, long acc, List<int[]>[] tree, int[] parent, int[] depth, long[] dist) {
        parent[u] = p;
        depth[u] = d;
        dist[u] = acc;
        for (int[] nei : tree[u]) {
            int v = nei[0], w = nei[1];
            if (v != p) {
                dfs(v, u, d + 1, acc + w, tree, parent, depth, dist);
            }
        }
    }
    private void flatten(int u, int p, List<int[]>[] tree, int[] tin, int[] tout, int[] nodeAt, int[] time) {
        tin[u] = time[0];
        nodeAt[time[0]] = u;
        time[0]++;
        for (int[] nei : tree[u]) {
            int v = nei[0];
            if (v != p) flatten(v, u, tree, tin, tout, nodeAt, time);
        }
        tout[u] = time[0] - 1;
    }
    private void update(long[] bit, int l, int r, int delta) {
        add(bit, l, delta);
        add(bit, r + 1, -delta);
    }
    private void add(long[] bit, int i, int delta) {
        int n = bit.length;
        while (i < n) { bit[i] += delta; i += i & -i; }
    }
    private long query(long[] bit, int i) {
        long res = 0;
        while (i > 0) { res += bit[i]; i -= i & -i; }
        return res;
    }
    private long key(int u, int v) {
        return ((long)Math.min(u, v) << 32) | Math.max(u, v);
    }
}
# @lc code=end