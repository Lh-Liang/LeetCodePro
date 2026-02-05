#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> graph(n);
        for (auto& inv : invocations) {
            graph[inv[0]].push_back(inv[1]);
        }
        // Step 1: Find all suspicious methods using BFS
        vector<bool> suspicious(n, false);
        queue<int> q;
        q.push(k);
        suspicious[k] = true;
        while (!q.empty()) {
            int curr = q.front(); q.pop();
            for (int nei : graph[curr]) {
                if (!suspicious[nei]) {
                    suspicious[nei] = true;
                    q.push(nei);
                }
            }
        }
        // Step 2: Check for outside invocations
        for (auto& inv : invocations) {
            int from = inv[0], to = inv[1];
            if (!suspicious[from] && suspicious[to]) {
                // Can't remove suspicious group
                vector<int> all(n);
                iota(all.begin(), all.end(), 0);
                return all;
            }
        }
        // Step 3: Return non-suspicious methods
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (!suspicious[i]) res.push_back(i);
        }
        return res;
    }
};
# @lc code=end