#
# @lc app=leetcode id=3604 lang=java
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
class Solution {
    public int minTime(int n, int[][] edges) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (int[] edge : edges) {
            adj.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2], edge[3]});
        }
        pq.offer(new int[]{0, 0}); // Start from node 0 at time 0.
        Map<Integer, Integer> visited = new HashMap<>();
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int node = current[0], time = current[1];
            if (node == n - 1) return time;
            if (visited.containsKey(node) && visited.get(node) <= time) continue;
            visited.put(node, time);
            for (int[] edge : adj.getOrDefault(node, Collections.emptyList())) {
                int nextNode = edge[0], startTime = edge[1], endTime = edge[2];
                if (time <= endTime) {
                    int newTime = Math.max(time + 1, startTime);
                    pq.offer(new int[]{nextNode, newTime});
                }
            }
        }
        return -1; // Return -1 if destination is unreachable.
    }
}
# @lc code=end