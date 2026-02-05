#
# @lc app=leetcode id=3710 lang=java
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution {
    public int maxPartitionFactor(int[][] points) {
        int n = points.length;
        if (n == 2) return 0;
        int left = 0, right = 400000001, ans = 0;
        // Precompute all pairwise Manhattan distances
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dist[i][j] = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
            }
        }
        while (left <= right) {
            int mid = left + (right - left) / 2;
            boolean possible = false;
            // Build graph: edge between i and j if dist[i][j] < mid
            List<Integer>[] graph = new List[n];
            for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    if (dist[i][j] < mid) {
                        graph[i].add(j);
                        graph[j].add(i);
                    }
                }
            }
            // Find connected components
            int[] comp = new int[n];
            Arrays.fill(comp, -1);
            int numComp = 0;
            for (int i = 0; i < n; ++i) {
                if (comp[i] == -1) {
                    Queue<Integer> q = new LinkedList<>();
                    q.add(i);
                    comp[i] = numComp;
                    while (!q.isEmpty()) {
                        int u = q.poll();
                        for (int v : graph[u]) {
                            if (comp[v] == -1) {
                                comp[v] = numComp;
                                q.add(v);
                            }
                        }
                    }
                    numComp++;
                }
            }
            if (numComp >= 2) possible = true;
            if (possible) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
}
# @lc code=end