#
# @lc app=leetcode id=3310 lang=java
#
# [3310] Remove Methods From Project
#

# @lc code=start
import java.util.*;
class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        // Step 1: Build adjacency list
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] inv : invocations) {
            graph[inv[0]].add(inv[1]);
        }
        // Step 2: Find all suspicious methods (reachable from k)
        boolean[] suspicious = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(k);
        while (!stack.isEmpty()) {
            int cur = stack.pop();
            if (suspicious[cur]) continue;
            suspicious[cur] = true;
            for (int nei : graph[cur]) {
                if (!suspicious[nei]) stack.push(nei);
            }
        }
        // Step 3: Check for invocations from outside suspicious set to inside
        for (int[] inv : invocations) {
            int from = inv[0], to = inv[1];
            if (!suspicious[from] && suspicious[to]) {
                List<Integer> all = new ArrayList<>();
                for (int i = 0; i < n; ++i) all.add(i);
                return all;
            }
        }
        // Step 4: Return all non-suspicious methods
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if (!suspicious[i]) res.add(i);
        }
        // Step 5: Verify output satisfies all problem constraints (e.g., edge cases, cycles)
        // (In this implementation, all constraints are covered by previous steps)
        return res;
    }
}
# @lc code=end