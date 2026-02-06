#
# @lc app=leetcode id=3425 lang=java
#
# [3425] Longest Special Path
#
# @lc code=start
class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
            graph.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(new int[]{edge[0], edge[2]});
        }
        return dfs(graph, nums, 0, new HashSet<>(), 0);
    }
    
    private int[] dfs(Map<Integer, List<int[]>> graph, int[] nums, int node, Set<Integer> visitedValues, int currentLength) {
        visitedValues.add(nums[node]);
        int maxLength = currentLength;
        int minNodes = 1;  // At least one node in path (itself)
        for (int[] neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visitedValues.contains(nums[neighbor[0]])) {
                Set<Integer> nextVisited = new HashSet<>(visitedValues);
                nextVisited.add(nums[neighbor[0]]);
                int[] result = dfs(graph, nums, neighbor[0], nextVisited, currentLength + neighbor[1]);
                if (result[0] > maxLength || (result[0] == maxLength && result[1] < minNodes)) {
                    maxLength = result[0];
                    minNodes = result[1];
                } 
            } 
        } 
        return new int[]{maxLength, minNodes}; 
    } 
}"# @lc code=end