#
# @lc app=leetcode id=3786 lang=java
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
import java.util.*;

class Solution {
    public long interactionCosts(int n, int[][] edges, int[] group) {
        // Step 1: Build adjacency list for the tree
        Map<Integer, List<Integer>> adjacencyList = new HashMap<>();
        for (int[] edge : edges) {
            adjacencyList.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            adjacencyList.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }
        
        // Step 2: Group nodes by their group labels
        Map<Integer, List<Integer>> groupNodes = new HashMap<>();
        for (int i = 0; i < n; i++) {
            groupNodes.computeIfAbsent(group[i], k -> new ArrayList<>()).add(i);
        }
        
        // Step 3: Calculate total interaction cost within each group
        long totalInteractionCost = 0;
        for (List<Integer> nodes : groupNodes.values()) {
            totalInteractionCost += calculateGroupInteractionCost(nodes, adjacencyList);
        }
        
        return totalInteractionCost;
    }
    
    private long calculateGroupInteractionCost(List<Integer> nodes, Map<Integer, List<Integer>> adjacencyList) {
        long groupCost = 0;
        int size = nodes.size();
        if (size < 2) return 0;
        
        // Use BFS/DFS to calculate pairwise distances within this group
        for (int node : nodes) {
            Map<Integer, Integer> distanceMap = bfs(node, adjacencyList);
            for (int target : nodes) {
                if (node != target) {
                    groupCost += distanceMap.getOrDefault(target, 0);
                }
            }
        }
        
       // Each pair was counted twice in an undirected graph scenario
       return groupCost / 2;
    }
    
    private Map<Integer, Integer> bfs(int startNode, Map<Integer, List<Integer>> adjacencyList) {				     				     				     				     	   	   	   	   	   	   	   	   	      Map<Integer,Integer> distanceMap = new HashMap<>();	      Queue<int[]> queue = new LinkedList<>(); queue.add(new int[]{startNode ,0}); distanceMap.put(startNode ,0); while(!queue.isEmpty()){	      int[] currentNode = queue.poll(); int currentDistance = currentNode[1]; int currentVertex = currentNode[0]; for(int neighbor : adjacencyList.get(currentVertex)){	      if(!distanceMap.containsKey(neighbor)){	      queue.add(new int[]{neighbor ,currentDistance+1}); distanceMap.put(neighbor ,currentDistance+1); } } } return distanceMap ; } } # @lc code=end