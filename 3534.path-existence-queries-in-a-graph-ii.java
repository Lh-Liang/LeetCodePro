# @lc code=start
class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        List<Integer>[] adj = new List[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; ++i) order[i] = i;
        java.util.Arrays.sort(order, java.util.Comparator.comparingInt(i -> nums[i]));
        int left = 0;
        for (int right = 0; right < n; ++right) {
            while (nums[order[right]] - nums[order[left]] > maxDiff) ++left;
            for (int i = left; i < right; ++i) {
                adj[order[right]].add(order[i]);
                adj[order[i]].add(order[right]);
            }
        }
        int[] parent = new int[n];
        for (int i = 0; i < n; ++i) parent[i] = i;
        for (int u = 0; u < n; ++u) {
            for (int v : adj[u]) {
                union(parent, u, v);
            }
        }
        int q = queries.length;
        int[] ans = new int[q];
        java.util.Map<Integer, java.util.List<Integer>> componentToQueries = new java.util.HashMap<>();
        for (int i = 0; i < q; ++i) {
            int u = queries[i][0];
            componentToQueries.computeIfAbsent(find(parent, u), k -> new java.util.ArrayList<>()).add(i);
        }
        for (int comp : componentToQueries.keySet()) {
            java.util.List<Integer> qIndices = componentToQueries.get(comp);
            java.util.Map<Integer, java.util.List<Integer>> srcToQueryIndices = new java.util.HashMap<>();
            for (int idx : qIndices) {
                int u = queries[idx][0];
                srcToQueryIndices.computeIfAbsent(u, k -> new java.util.ArrayList<>()).add(idx);
            }
            java.util.Map<Integer, java.util.Map<Integer, Integer>> srcToDist = new java.util.HashMap<>();
            for (int src : srcToQueryIndices.keySet()) {
                java.util.Map<Integer, Integer> dists = bfsAll(src, adj, n);
                srcToDist.put(src, dists);
            }
            for (int src : srcToQueryIndices.keySet()) {
                for (int idx : srcToQueryIndices.get(src)) {
                    int v = queries[idx][1];
                    if (src == v) {
                        ans[idx] = 0;
                    } else {
                        java.util.Map<Integer, Integer> dists = srcToDist.get(src);
                        ans[idx] = dists.getOrDefault(v, -1);
                    }
                }
            }
        }
        return ans;
    }
    private int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
    private void union(int[] parent, int x, int y) {
        int px = find(parent, x), py = find(parent, y);
        if (px != py) parent[py] = px;
    }
    private java.util.Map<Integer, Integer> bfsAll(int src, List<Integer>[] adj, int n) {
        java.util.Map<Integer, Integer> dist = new java.util.HashMap<>();
        boolean[] visited = new boolean[n];
        java.util.Queue<Integer> q = new java.util.ArrayDeque<>();
        q.offer(src);
        visited[src] = true;
        dist.put(src, 0);
        int d = 0;
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                int u = q.poll();
                for (int v : adj[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        dist.put(v, d + 1);
                        q.offer(v);
                    }
                }
            }
            ++d;
        }
        return dist;
    }
}
# @lc code=end