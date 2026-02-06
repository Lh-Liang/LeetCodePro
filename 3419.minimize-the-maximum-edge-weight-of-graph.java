#
# @lc app=leetcode id=3419 lang=java
#
# [3419] Minimize the Maximum Edge Weight of Graph
#
# @lc code=start
import java.util.*;
class Solution {
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        int left = 1, right = 1000000, answer = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isFeasible(n, edges, threshold, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }
    private boolean isFeasible(int n, int[][] edges, int threshold, int maxWeight) {
        // Map from node to list of outgoing edges (to, weight)
        List<int[]>[] graph = new List[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            if (e[2] <= maxWeight) {
                graph[e[0]].add(new int[]{e[1], e[2]});
            }
        }
        // For each node, keep only threshold outgoing edges with smallest weights
        for (int i = 0; i < n; ++i) {
            List<int[]> list = graph[i];
            if (list.size() > threshold) {
                list.sort(Comparator.comparingInt(a -> a[1]));
                while (list.size() > threshold) list.remove(list.size() - 1);
            }
        }
        // Build reverse graph for BFS from 0
        List<Integer>[] reverse = new List[n];
        for (int i = 0; i < n; ++i) reverse[i] = new ArrayList<>();
        for (int u = 0; u < n; ++u) {
            for (int[] v : graph[u]) {
                reverse[v[0]].add(u);
            }
        }
        // BFS from node 0 over reverse graph
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0); visited[0] = true;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int prev : reverse[curr]) {
                if (!visited[prev]) {
                    visited[prev] = true;
                    queue.add(prev);
                }
            }
        }
        // Check if all nodes can reach 0
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) return false;
        }
        return true;
    }
}
# @lc code=end