#
# @lc app=leetcode id=3310 lang=java
#
# [3310] Remove Methods From Project
#
# @lc code=start
import java.util.*;
class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        // Step 1: Build the adjacency list for graph traversal
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] edge : invocations) {
            graph[edge[0]].add(edge[1]);
        }
        // Step 2: Find all suspicious methods via BFS
        Set<Integer> suspicious = new HashSet<>();
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(k);
        suspicious.add(k);
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int nei : graph[curr]) {
                if (suspicious.add(nei)) {
                    queue.add(nei);
                }
            }
        }
        // Step 3: Check for any external invocation into suspicious
        for (int[] edge : invocations) {
            int from = edge[0], to = edge[1];
            if (!suspicious.contains(from) && suspicious.contains(to)) {
                // There is an external invocation
                List<Integer> all = new ArrayList<>();
                for (int i = 0; i < n; ++i) all.add(i);
                return all;
            }
        }
        // Step 4: Return non-suspicious methods
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; ++i) if (!suspicious.contains(i)) res.add(i);
        return res;
    }
}
# @lc code=end