#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#

# @lc code=start
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Step 1: Build the adjacency list for the graph
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        // Step 2: Identify all suspicious methods using BFS
        vector<bool> isSuspicious(n, false);
        queue<int> q;
        q.push(k);
        isSuspicious[k] = true;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!isSuspicious[v]) {
                    isSuspicious[v] = true;
                    q.push(v);
                }
            }
        }

        // Step 3: Check if any method outside the suspicious set invokes any method inside it
        bool canRemove = true;
        for (const auto& inv : invocations) {
            int u = inv[0];
            int v = inv[1];
            // If source is not suspicious but target is, we cannot remove the group
            if (!isSuspicious[u] && isSuspicious[v]) {
                canRemove = false;
                break;
            }
        }

        // Step 4: Collect the remaining methods based on the removal check
        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (!canRemove || !isSuspicious[i]) {
                result.push_back(i);
            }
        }
        
        return result;
    }
};
# @lc code=end