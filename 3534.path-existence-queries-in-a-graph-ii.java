#
# @lc app=leetcode id=3534 lang=java
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        // Step 1: Construct the graph based on nums and maxDiff.
        List<Integer>[] adjList = new ArrayList[n];
        for (int i = 0; i < n; i++) adjList[i] = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(nums[i] - nums[j]) <= maxDiff) {
                    adjList[i].add(j);
                    adjList[j].add(i);
                }
            }
        }
        // Step 2: Handle queries using BFS/Union-Find for path existence.
        int[] result = new int[queries.length];
        Arrays.fill(result, -1); // Initially assume no paths exist.
        for (int qi = 0; qi < queries.length; qi++) {
            int[] query = queries[qi];
            if (query[0] == query[1]) { // Same node case.
                result[qi] = 0; continue; 
            } 
            // BFS Approach: Check connectivity. 
            Queue<Integer> queue = new LinkedList<>(); 
            boolean[] visited = new boolean[n]; 
            queue.add(query[0]); visited[query[0]] = true; 
            boolean found = false; int dist = 0; 
            while (!queue.isEmpty() && !found) { 
                dist++; int size = queue.size(); 
                for (int s = 0; s < size && !found; s++) { 
                    int node = queue.poll(); 
                    for (int neighbor : adjList[node]) { 
                        if (!visited[neighbor]) { 
                            if (neighbor == query[1]) { found = true; break; } 
                            queue.add(neighbor); visited[neighbor] = true; 
                        } 
                    } 
                } ​} if(found) result[qi] = dist - 1; // Adjust distance as needed. ​} return result;} } # @lc code=end