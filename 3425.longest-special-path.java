#
# @lc app=leetcode id=3425 lang=java
#
# [3425] Longest Special Path
#

# @lc code=start
import java.util.*;

class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        // Convert edges into adjacency list
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
            graph.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(new int[]{edge[0], edge[2]});
        }
        // Variables to track max length and min nodes count
        int[] maxLengthAndMinNodes = new int[]{0, Integer.MAX_VALUE};
        // DFS function to explore paths
        dfs(0, -1, nums, graph, new HashSet<>(), 0, 0, maxLengthAndMinNodes);
        return maxLengthAndMinNodes;
    }
    
    private void dfs(int node, int parent, int[] nums, Map<Integer, List<int[]>> graph,
                     Set<Integer> visitedValues, int currentLength, int currentNodeCount,
                     int[] maxLengthAndMinNodes) {
        visitedValues.add(nums[node]);
        currentNodeCount++;
        for (int[] neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (neighbor[0] != parent && !visitedValues.contains(nums[neighbor[0]])) {
                visitedValues.add(nums[neighbor[0]]);
                dfs(neighbor[0], node, nums, graph, visitedValues,
                    currentLength + neighbor[1], currentNodeCount,
                    maxLengthAndMinNodes);
                visitedValues.remove(nums[neighbor[0]]);  // Backtrack
            }
        }
        if (currentLength > maxLengthAndMinNodes[0]) {
            maxLengthAndMinNodes[0] = currentLength;
            maxLengthAndMinNodes[1] = currentNodeCount;
        } else if (currentLength == maxLengthAndMinNodes[0]) {
            maxLengthAndMinNodes[1] = Math.min(maxLengthAndMinNodes[1], currentNodeCount);
        }
    }
}
# @lc code=end