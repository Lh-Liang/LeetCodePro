// @lc app=leetcode id=3534 lang=java
//
// [3534] Path Existence Queries in a Graph II
//

// @lc code=start
class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        // Initialize union-find structure.
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
        
        // Create array of index-value pairs and sort by value.
        int[][] indexValuePairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            indexValuePairs[i][0] = nums[i];
            indexValuePairs[i][1] = i;
        }
        Arrays.sort(indexValuePairs, Comparator.comparingInt(pair -> pair[0]));

        // Use two pointers to find valid edges based on maxDiff.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n && indexValuePairs[j][0] - indexValuePairs[i][0] <= maxDiff; j++) {
                union(indexValuePairs[i][1], indexValuePairs[j][1], parent, rank);
            }
        }

        // Prepare answers for queries using find operation.
        int[] answer = new int[queries.length];
        for (int k = 0; k < queries.length; k++) {
            int u = queries[k][0];
            int v = queries[k][1];
            answer[k] = find(u, parent) == find(v, parent) ? 1 : -1;
        }
        return answer;
    }
    
    private int find(int x, int[] parent) {
        if (parent[x] != x) {
            parent[x] = find(parent[x], parent); // Path compression
        }
        return parent[x];
    }
    
    private void union(int x, int y, int[] parent, int[] rank) {
        int rootX = find(x, parent);
        int rootY = find(y, parent);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}
// @lc code=end