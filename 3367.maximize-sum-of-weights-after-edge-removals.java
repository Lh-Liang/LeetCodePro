# @lc app=leetcode id=3367 lang=java
# [3367] Maximize Sum of Weights after Edge Removals
#
# @lc code=start
class Solution {
    public long maximizeSumOfWeights(int[][] edges, int k) {
        // Step 1: Create adjacency lists for representing the graph.
        Map<Integer, List<int[]>> graph = new HashMap<>(); // Node -> List of [neighbor, weight]
        long totalWeight = 0;
        
        // Step 2: Populate the adjacency list and calculate total weight sum.
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph.computeIfAbsent(u, x -> new ArrayList<>()).add(new int[]{v, w});
            graph.computeIfAbsent(v, x -> new ArrayList<>()).add(new int[]{u, w});
            totalWeight += w;
        }
        
        // Step 3: Sort edges by weight in descending order to prioritize removals.
        Arrays.sort(edges, (a, b) -> Integer.compare(b[2], a[2]));

        // Step 4: Tracking node degrees and applying removal logic using max spanning tree concepts.
        Map<Integer, Integer> degree = new HashMap<>();
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0], v = edges[i][1];
            degree.put(u, degree.getOrDefault(u, 0) + 1);
            degree.put(v, degree.getOrDefault(v, 0) + 1);
        }

        // Step 5: Process edges and validate conditions globally across the graph.
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (degree.get(u) > k || degree.get(v) > k) {
                // Only remove if it helps in reducing excess connections
                totalWeight -= w;
                degree.put(u, degree.get(u) - 1);
                degree.put(v, degree.get(v) - 1);
            }
        }

        return totalWeight;
    }
}
# @lc code=end