#
# @lc app=leetcode id=3310 lang=java
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        Set<Integer> suspicious = new HashSet<>();
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, List<Integer>> reverseGraph = new HashMap<>();
        
        // Build graph and reverse graph for easy traversal
        for (int[] invocation : invocations) {
            graph.computeIfAbsent(invocation[0], x -> new ArrayList<>()).add(invocation[1]);
            reverseGraph.computeIfAbsent(invocation[1], x -> new ArrayList<>()).add(invocation[0]);
        }
        
        // Use BFS to find all reachable nodes from k (suspicious nodes)
        Queue<Integer> queue = new LinkedList<>();
        queue.add(k);
        while (!queue.isEmpty()) {
            int method = queue.poll();
            if (suspicious.add(method)) { // Add if not already visited/suspicious
                List<Integer> children = graph.get(method);
                if (children != null) { queue.addAll(children); } 
            }  
        }
        
        // Validate: Check that no non-suspicious node invokes any suspicious node
        for (int node : suspicious) {
            List<Integer> invokers = reverseGraph.get(node);
            if (invokers != null) {
                for (int invoker : invokers) {
                    if (!suspicious.contains(invoker)) {
                        return IntStream.range(0, n).boxed().collect(Collectors.toList()); // Return all nodes
                    }
                }
            }
        }

        // If valid, return only non-suspicious nodes
        return IntStream.range(0, n)
                        .filter(method -> !suspicious.contains(method))
                        .boxed().collect(Collectors.toList());
    }
}
# @lc code=end