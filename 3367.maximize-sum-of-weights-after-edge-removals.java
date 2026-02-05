#
# @lc app=leetcode id=3367 lang=java
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
// Step-by-step approach:
// 1. Build an adjacency list and a map for edge weights.
// 2. Compute degrees for all nodes.
// 3. For each node with degree > k, remove lowest-weight incident edges, updating degrees for both endpoints and marking removed edges.
// 4. Ensure no edge is removed twice, and verify all degrees <= k after removals.
// 5. Sum weights of remaining edges.
class Solution {
    public long maximizeSumOfWeights(int[][] edges, int k) {
        // Step 1: Build adjacency list and edge index map
        int n = edges.length + 1;
        Map<Integer, List<int[]>> adj = new HashMap<>(); // node -> list of [neighbor, weight, edgeId]
        Map<String, Integer> edgeWeight = new HashMap<>(); // "u,v" -> weight
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            adj.computeIfAbsent(u, x -> new ArrayList<>()).add(new int[]{v, w, i});
            adj.computeIfAbsent(v, x -> new ArrayList<>()).add(new int[]{u, w, i});
            edgeWeight.put(u + "," + v, w);
            edgeWeight.put(v + "," + u, w);
        }
        // Step 2: Compute degrees
        int[] degree = new int[n];
        for (int i = 0; i < n; i++) degree[i] = adj.getOrDefault(i, new ArrayList<>()).size();
        // Step 3: For each node with degree > k, mark lightest edges for removal
        Set<Integer> removedEdges = new HashSet<>();
        boolean changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i < n; i++) {
                if (degree[i] > k) {
                    // sort incident edges by weight
                    List<int[]> incident = new ArrayList<>();
                    for (int[] nei : adj.get(i)) {
                        if (!removedEdges.contains(nei[2])) {
                            incident.add(nei);
                        }
                    }
                    incident.sort(Comparator.comparingInt(a -> a[1]));
                    int removeCount = degree[i] - k;
                    for (int j = 0, cnt = 0; j < incident.size() && cnt < removeCount; j++) {
                        int neighbor = incident.get(j)[0];
                        int edgeId = incident.get(j)[2];
                        if (removedEdges.contains(edgeId)) continue;
                        removedEdges.add(edgeId);
                        degree[i]--;
                        degree[neighbor]--;
                        changed = true;
                        cnt++;
                    }
                }
            }
        }
        // Step 5: Sum the weights of remaining edges
        long total = 0L;
        for (int i = 0; i < edges.length; i++) {
            if (!removedEdges.contains(i)) {
                total += edges[i][2];
            }
        }
        // Step 7: Final verification
        // (Optional, as above loop ensures no degree > k)
        return total;
    }
}
# @lc code=end