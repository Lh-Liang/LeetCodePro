#
# @lc app=leetcode id=3710 lang=java
#
# [3710] Maximum Partition Factor
#

# @lc code=start
import java.util.*;
class Solution {
    public int maxPartitionFactor(int[][] points) {
        int n = points.length;
        if (n == 2) return 0; // Special case: both groups singletons
        // Collect all unique pairwise Manhattan distances
        TreeSet<Integer> dists = new TreeSet<>();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int d = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                dists.add(d);
            }
        }
        List<Integer> candidates = new ArrayList<>(dists);
        int lo = 0, hi = candidates.size() - 1;
        int ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int cand = candidates.get(mid);
            if (canSplit(points, cand)) {
                ans = cand;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
    // Returns true if points can be split into 2 groups so all intra-group pairs have distance >= d
    private boolean canSplit(int[][] points, int d) {
        int n = points.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; ++i) graph.add(new ArrayList<>());
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                if (dist < d) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        int[] color = new int[n]; // 0: unvisited, 1: color1, -1: color2
        for (int i = 0; i < n; ++i) {
            if (color[i] == 0) {
                if (!bfs(i, graph, color)) return false;
            }
        }
        return true;
    }
    private boolean bfs(int start, List<List<Integer>> graph, int[] color) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        color[start] = 1;
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nei : graph.get(node)) {
                if (color[nei] == 0) {
                    color[nei] = -color[node];
                    q.add(nei);
                } else if (color[nei] == color[node]) {
                    return false;
                }
            }
        }
        return true;
    }
}
# @lc code=end