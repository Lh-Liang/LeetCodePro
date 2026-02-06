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
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(new int[]{e[1], e[2], e[3]});
        }
        int[] earliest = new int[n];
        Arrays.fill(earliest, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0}); // (currentTime, node)
        earliest[0] = 0;
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int time = cur[0], node = cur[1];
            if (node == n - 1) return time;
            if (time > earliest[node]) continue;
            for (int[] edge : graph[node]) {
                int nei = edge[0], start = edge[1], end = edge[2];
                int depart = Math.max(time, start);
                if (depart > end) continue;
                int arrive = depart + 1;
                if (arrive < earliest[nei]) {
                    earliest[nei] = arrive;
                    pq.offer(new int[]{arrive, nei});
                }
            }
        }
        return -1;
    }
}
# @lc code=end