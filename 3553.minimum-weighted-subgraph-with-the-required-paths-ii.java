#
# @lc app=leetcode id=3553 lang=java
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

import java.util.*;

class Solution {
    private static final long INF = Long.MAX_VALUE;
    
    public int[] minimumWeight(int[][] edges, int[][] queries) {
        int n = edges.length + 1; // As it's a tree with n-1 edges
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        // Build graph
        for (int[] edge : edges) {
            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
            graph.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int src1 = queries[i][0];
            int src2 = queries[i][1];
            int dest = queries[i][2];
            
            long[] distFromSrc1 = dijkstra(graph, src1, n);
            long[] distFromSrc2 = dijkstra(graph, src2, n);
            long[] distFromDest = dijkstra(graph, dest, n);
            
            long minWeight = INF;
            for (int v = 0; v < n; v++) {
                if (distFromSrc1[v] != INF && distFromSrc2[v] != INF && distFromDest[v] != INF) {
                    minWeight = Math.min(minWeight, distFromSrc1[v] + distFromSrc2[v] + distFromDest[v]);
                }
            }
            result[i] = minWeight == INF ? -1 : (int)minWeight;
        }
        return result;
    }
    
    private long[] dijkstra(List<List<int[]>> graph, int start, int n) {		PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));		long[] dist = new long[n];		Arrays.fill(dist, INF);  		pq.offer(new long[]{0L, start});		dist[start] = 0;		while (!pq.isEmpty()) { 			long[] curr = pq.poll(); 			long currDist = curr[0]; 			int u = (int)curr[1]; 			if (currDist > dist[u]) continue;			for (int[] neighbor : graph.get(u)) { 				int v = neighbor[0]; 				long weightUV = neighbor[1]; 	 if (dist[u] + weightUV < dist[v]) { 		dist[v] = dist[u] + weightUV; 		pq.offer(new long[]{dist[v], v}); 	} } } return dist; } }