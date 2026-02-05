# @lc app=leetcode id=3373 lang=java
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
class Solution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2) {
        // Step 1: Convert edge lists to adjacency lists.
        List<Integer>[] tree1 = buildAdjacencyList(edges1);
        List<Integer>[] tree2 = buildAdjacencyList(edges2);
        
        // Step 2: Calculate depths using BFS for both trees.
        int[] depth1 = calculateDepths(tree1);
        int[] depth2 = calculateDepths(tree2);
        
        // Step 3: Iterate over each node in the first tree.
        int n = edges1.length + 1;
        int m = edges2.length + 1;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            // Step 4: Simulate connecting this node with every node in second tree and find max targets.
            result[i] = calculateMaxTargets(i, depth1, depth2, m);
        }

        return result;
    }

    private List<Integer>[] buildAdjacencyList(int[][] edges) {
        int n = edges.length + 1;
        List<Integer>[] adjList = new ArrayList[n];
        for (int i = 0; i < n; i++) adjList[i] = new ArrayList<>();
        for (int[] edge : edges) {
            adjList[edge[0]].add(edge[1]);
            adjList[edge[1]].add(edge[0]);
        }
        return adjList;
    }

    private int[] calculateDepths(List<Integer>[] tree) {
       int n = tree.length;
       int[] depths = new int[n];
       boolean[] visited = new boolean[n];
       Queue<Integer> queue = new LinkedList<>();
       queue.add(0); // Start BFS from an arbitrary root, say node 0
       visited[0] = true;

       while (!queue.isEmpty()) {
           int node = queue.poll();
           for (int neighbor : tree[node]) {
               if (!visited[neighbor]) {
                   visited[neighbor] = true;
                   depths[neighbor] = depths[node] + 1;
                   queue.add(neighbor);
               }
           }								   	   			   	   	   	   	    	   	   	    	   	   	    	    }     }     return depths;     }     private int calculateMaxTargets(int i, int[] depth1, int[] depth2, int m) {         // Calculate max targets possible by connecting node `i` from tree1 with each node from tree2         int maxTargets = 0;         for (int j = 0; j < m; j++) {             // If path length is even, increase target count             if ((depth1[i] + depth2[j]) % 2 == 0) {                 maxTargets++;             }         }         return maxTargets;     } }