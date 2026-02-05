// @lc app=leetcode id=3486 lang=java
//
// [3486] Longest Special Path II
//
// @lc code=start
import java.util.*;
class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        // Convert edge list to adjacency list
        Map<Integer, List<int[]>> adjList = new HashMap<>();
        for (int[] edge : edges) {
            adjList.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
            adjList.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(new int[]{edge[0], edge[2]});
        }
        // Result array: [maxLength, minNodes]
        int[] result = new int[]{0, Integer.MAX_VALUE};
        // Helper function for DFS traversal
        dfs(0, -1, 0, 0, new HashMap<>(), nums, adjList, result);
        return result;
    }
    private void dfs(int node, int parent, int length, int nodesCount,
                     Map<Integer, Integer> valueCount,
                     int[] nums,
                     Map<Integer, List<int[]>> adjList,
                     int[] result) {
        valueCount.put(nums[node], valueCount.getOrDefault(nums[node], 0) + 1);
        boolean canContinue = true;
        if (valueCount.get(nums[node]) > 2 ||
            (valueCount.get(nums[node]) == 2 && valueCount.values().stream().filter(v -> v == 2).count() > 1)) {
            canContinue = false;
        }
        if (canContinue) {
            for (int[] neighbor : adjList.get(node)) {
                if (neighbor[0] != parent) { // Avoid revisiting parent node
                    dfs(neighbor[0], node, length + neighbor[1], nodesCount + 1,
                        valueCount, nums, adjList, result);
                }
            }
            // Update result if this path is longer or equally long but with fewer nodes.
            if (length > result[0] || (length == result[0] && nodesCount < result[1])) {
                result[0] = length;
                result[1] = nodesCount;
            }
        }
n// Backtrack by removing current node's value from map.
nvalueCount.put(nums[node], valueCount.get(nums[node]) - 1);
nif (valueCount.get(nums[node]) == 0) { 
nvalueCount.remove(nums[node]); 
n}
n}
n}
n// @lc code=end