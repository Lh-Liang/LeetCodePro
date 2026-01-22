#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Build adjacency list
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            int a = inv[0], b = inv[1];
            adj[a].push_back(b);
        }
        
        // Mark all methods reachable from k as suspicious using BFS
        vector<bool> suspicious(n, false);
        queue<int> q;
        q.push(k);
        suspicious[k] = true;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    q.push(v);
                }
            }
        }
        
        // Check if any method outside the suspicious set invokes a method inside
        bool canRemove = true;
        for (const auto& inv : invocations) {
            int a = inv[0], b = inv[1];
            if (suspicious[b] && !suspicious[a]) {
                canRemove = false;
                break;
            }
        }
        
        if (!canRemove) {
            // Cannot remove any; return all methods
            vector<int> res(n);
            iota(res.begin(), res.end(), 0);
            return res;
        } else {
            // Remove all suspicious methods
            vector<int> res;
            for (int i = 0; i < n; ++i) {
                if (!suspicious[i]) {
                    res.push_back(i);
                }
            }
            return res;
        }
    }
};
# @lc code=end