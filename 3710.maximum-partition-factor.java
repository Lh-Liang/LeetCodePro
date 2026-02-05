#
# @lc app=leetcode id=3710 lang=java
#
# [3710] Maximum Partition Factor
#
# @lc code=start
class Solution {
    public int maxPartitionFactor(int[][] points) {
        // Initialize variables for maximum partition factor calculation.
        int maxPartitionFactor = 0;
        
        // Calculate pairwise Manhattan distances between all points.
        int n = points.length;
        int[] manhattanDistances = new int[(n * (n - 1)) / 2];
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                manhattanDistances[index++] = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
            }
        }
        
        // Sort the distances to find feasible partitions quickly
        Arrays.sort(manhattanDistances);

        // Binary search over possible partition factors (distances)
        int low = 0, high = manhattanDistances.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canPartition(points, manhattanDistances[mid])) {
                maxPartitionFactor = manhattanDistances[mid];
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return maxPartitionFactor;
    }
    
    private boolean canPartition(int[][] points, int minDistance) {		// Implement logic using union-find to check if valid partitions exist with given minDistance.		// Initialize union-find structure.		UnionFind uf = new UnionFind(points.length);		// Iterate over all pairs of points and union them if their distance is less than minDistance.		for (int i = 0; i < points.length; i++) {		for (int j = i + 1; j < points.length; j++) {		if (Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]) < minDistance) {		uf.union(i, j);		}		}		}		// Check if there are at least two components formed by this union-find structure.		return uf.getCount() >= 2;	}	// Define UnionFind class to manage connected components efficiently.class UnionFind {private int[] parent;private int count;public UnionFind(int size) {parent = new int[size];count = size;for (int i = 0; i < size; i++) {parent[i] = i;} }public void union(int x, int y) {int rootX = find(x);int rootY = find(y);if (rootX != rootY) {parent[rootY] = rootX;count--;}}public int find(int x) {if (parent[x] != x) {parent[x] = find(parent[x]);}return parent[x];}public int getCount() {return count;} }	 \\\/\\\\\\\\\\\
}# @lc code=end