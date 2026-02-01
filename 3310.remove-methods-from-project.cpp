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
        // Build adjacency list for the graph
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        // Find all suspicious methods using BFS starting from k
        vector<bool> isSuspicious(n, false);
        isSuspicious[k] = true;
        queue<int> q;
        q.push(k);

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

        // Check if any method outside the suspicious group invokes a method inside it
        bool canRemove = true;
        for (const auto& inv : invocations) {
            if (!isSuspicious[inv[0]] && isSuspicious[inv[1]]) {
                canRemove = false;
                break;
            }
        }

        // Construct the result based on whether the suspicious group can be removed
        vector<int> result;
        if (canRemove) {
            for (int i = 0; i < n; ++i) {
                if (!isSuspicious[i]) {
                    result.push_back(i);
                }
            }
        } else {
            for (int i = 0; i < n; ++i) {
                result.push_back(i);
            }
        }

        return result;
    }
};
# @lc code=end