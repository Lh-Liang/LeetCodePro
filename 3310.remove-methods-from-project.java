#
# @lc app=leetcode id=3310 lang=java
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        // Step 1: Build graph from invocations
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : invocations) {
            graph[edge[0]].add(edge[1]);
        }
        
        // Step 2: Find all suspicious methods starting from k using DFS
        Set<Integer> suspicious = new HashSet<>();
        dfs(k, graph, suspicious);
        
        // Step 3: Check if any method outside suspicious invokes any within it
        boolean[] invokedByOutside = new boolean[n];
        for (int[] edge : invocations) {
            if (!suspicious.contains(edge[0]) && suspicious.contains(edge[1])) {
                invokedByOutside[edge[1]] = true;
            }
        }
        for (int method : suspicious) {
            if (invokedByOutside[method]) {
                return IntStream.range(0, n).boxed().collect(Collectors.toList()); // Return all methods if condition not met. 
            } 
        } 
        
        // Step 4: Return remaining methods after removing suspicious ones if possible. 
        List<Integer> remainingMethods = new ArrayList<>(); 
        for (int i = 0; i < n; i++) { 
            if (!suspicious.contains(i)) { 
                remainingMethods.add(i); 
            } 
        }  return remainingMethods;  } private void dfs(int node, List<Integer>[] graph, Set<Integer> visited) { if (visited.contains(node)) return; visited.add(node); for (int neighbor : graph[node]) dfs(neighbor, graph, visited); } # @lc code=end