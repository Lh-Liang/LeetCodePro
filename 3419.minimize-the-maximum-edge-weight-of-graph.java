#
# @lc app=leetcode id=3419 lang=java
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        // Sort edges by weight (ascending)
        Arrays.sort(edges, Comparator.comparingInt(a -> a[2]));
        
        // Union-Find setup to ensure node 0 is reachable from all nodes
        UnionFind uf = new UnionFind(n);
        
        // Priority Queue to manage outgoing edge constraints per node
        Map<Integer, PriorityQueue<int[]>> outEdges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            outEdges.put(i, new PriorityQueue<>(Comparator.comparingInt(a -> -a[2]))); // Max-heap by weight
        }
        
        int maxWeight = -1; // Track maximum edge weight in result graph
        
        for (int[] edge : edges) {
            int from = edge[0], to = edge[1], weight = edge[2];
            
            if (uf.connected(to, 0)) continue; // If 'to' is already connected to 0 skip this edge as unnecessary.
            
            // Add current edge to node's outgoing list and check constraint.
            outEdges.get(from).offer(edge);
            if (outEdges.get(from).size() > threshold) {
                outEdges.get(from).poll(); // Remove heaviest if exceeding threshold.
            } else {
                uf.union(from, to); // Union nodes as they are added under threshold.
                maxWeight = Math.max(maxWeight, weight); // Update maximum weight needed so far.
            }          	         	      	   	         	       	      	   	          	         	     	       	     }    }    return uf.connected(0) ? maxWeight : -1;    }    class UnionFind {    private int[] parent;    private int[] rank;    public UnionFind(int size) {    parent = new int[size];    rank = new int[size];    for (int i = 0; i < size; i++) {    parent[i] = i;    rank[i] = 1;    }}public boolean connected(int x, int y) {return find(x) == find(y);}public void union(int x, int y) {int rootX = find(x), rootY = find(y);if (rootX != rootY) {if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;else if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;else {parent[rootY] = rootX;rank[rootX]++;}}}private int find(int x) {if (x != parent[x])parent[x] = find(parent[x]);return parent[x];}}} # @lc code=end