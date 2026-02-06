#
# @lc app=leetcode id=3786 lang=java
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution {
    public long interactionCosts(int n, int[][] edges, int[] group) {
        // Create adjacency list from edges
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        
        // Map to store group-wise nodes
        Map<Integer, List<Integer>> groupMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            groupMap.computeIfAbsent(group[i], k -> new ArrayList<>()).add(i);
        }
        
        // Function to calculate interaction cost using DFS
        long totalCost = 0;
        for (int grp : groupMap.keySet()) {
            List<Integer> nodes = groupMap.get(grp);
            if (nodes.size() < 2) continue; // Single node can't form a pair
            
            boolean[] visited = new boolean[n];
            for (int node : nodes) {
                Arrays.fill(visited, false); // Reset visited array for each node in group
                totalCost += dfs(adjList, visited, node, -1); // Calculate cost from current node to others in its group & add to total cost & avoid double counting pairs by starting with -1 depth. & track depth of traversal from current node. & depth gives distance between nodes forming pair. & return sum of all such valid distances. & recursively call dfs on each adjacent unvisited node until no more such nodes exist or max depth is achieved.