#
# @lc app=leetcode id=3604 lang=java
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
import java.util.*;
class Solution {
    public int minTime(int n, int[][] edges) {
        List<int[]>[] graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            // e = [u, v, start, end]
            graph[e[0]].add(new int[]{e[1], e[2], e[3]});
        }
        // min-heap: [current time, node]
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0});
        int[] minArrival = new int[n];
        Arrays.fill(minArrival, Integer.MAX_VALUE);
        minArrival[0] = 0;
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int time = curr[0], node = curr[1];
            if (node == n - 1) return time;
            if (time > minArrival[node]) continue;
            for (int[] edge : graph[node]) {
                int next = edge[0], start = edge[1], end = edge[2];
                if (time > end) continue; // Can't take this edge anymore
                int depart = Math.max(time, start); // Wait if needed
                if (depart > end) continue;
                int arrive = depart + 1;
                if (arrive < minArrival[next]) {
                    minArrival[next] = arrive;
                    pq.offer(new int[]{arrive, next});
                }
            }
        }
        return -1;
    }
}
# @lc code=end