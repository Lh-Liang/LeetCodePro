#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Build the graph: adjacency list
        vector<vector<int>> graph(n);
        for (const auto& inv : invocations) {
            graph[inv[0]].push_back(inv[1]);
        }
        // Step 1: Collect all suspicious methods (reachable from k)
        vector<bool> suspicious(n, false);
        queue<int> q;
        q.push(k);
        suspicious[k] = true;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : graph[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    q.push(v);
                }
            }
        }
        // Step 2: Check for external invocations into suspicious set
        for (const auto& inv : invocations) {
            int from = inv[0], to = inv[1];
            if (!suspicious[from] && suspicious[to]) {
                // Found external invocation; cannot remove suspicious methods
                vector<int> res(n);
                for (int i = 0; i < n; ++i) res[i] = i;
                return res;
            }
        }
        // Step 3: Construct the result with non-suspicious methods
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (!suspicious[i]) res.push_back(i);
        }
        // Step 4: Verify that the result meets all constraints
        // (No external invocations into suspicious set; all suspicious methods identified)
        // Step 5: Handle edge cases implicitly by construction
        return res;
    }
};
# @lc code=end