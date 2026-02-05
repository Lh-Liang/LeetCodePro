#
# @lc app=leetcode id=3419 lang=java
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        // Step 1: Find all unique edge weights for binary search
        TreeSet<Integer> weights = new TreeSet<>();
        for (int[] e : edges) weights.add(e[2]);
        Integer[] sortedWeights = weights.toArray(new Integer[0]);
        int left = 0, right = sortedWeights.length - 1, ans = -1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int maxW = sortedWeights[mid];
            // Build subgraph with only edges of weight <= maxW
            ArrayList<int[]>[] outgoing = new ArrayList[n];
            for (int i = 0; i < n; ++i) {
                outgoing[i] = new ArrayList<>();
            }
            for (int[] e : edges) {
                if (e[2] <= maxW) {
                    outgoing[e[0]].add(new int[]{e[2], e[1]});
                }
            }
            // For each node, keep only up to 'threshold' smallest-weight outgoing edges
            ArrayList<Integer>[] graph = new ArrayList[n];
            for (int i = 0; i < n; ++i) {
                outgoing[i].sort((a, b) -> a[0] - b[0]);
                graph[i] = new ArrayList<>();
                for (int j = 0; j < Math.min(threshold, outgoing[i].size()); ++j) {
                    graph[i].add(outgoing[i].get(j)[1]);
                }
            }
            // Reverse the graph for efficient reachability check from node 0
            ArrayList<Integer>[] reverseGraph = new ArrayList[n];
            for (int i = 0; i < n; ++i) reverseGraph[i] = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                for (int v : graph[i]) {
                    reverseGraph[v].add(i);
                }
            }
            // BFS from node 0 in reversed graph
            boolean[] visited = new boolean[n];
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(0);
            visited[0] = true;
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int v : reverseGraph[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        queue.offer(v);
                    }
                }
            }
            boolean valid = true;
            for (int i = 1; i < n; ++i) {
                if (!visited[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                ans = maxW;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
}
# @lc code=end