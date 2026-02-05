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
        // Build adjacency list for reachability
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        // Find all suspicious methods using BFS
        vector<bool> is_suspicious(n, false);
        queue<int> q;
        q.push(k);
        is_suspicious[k] = true;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            for (int neighbor : adj[curr]) {
                if (!is_suspicious[neighbor]) {
                    is_suspicious[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        // Check if any non-suspicious method invokes a suspicious method
        bool can_remove = true;
        for (const auto& inv : invocations) {
            if (!is_suspicious[inv[0]] && is_suspicious[inv[1]]) {
                can_remove = false;
                break;
            }
        }

        // Prepare the result list
        vector<int> res;
        if (can_remove) {
            for (int i = 0; i < n; ++i) {
                if (!is_suspicious[i]) res.push_back(i);
            }
        } else {
            for (int i = 0; i < n; ++i) {
                res.push_back(i);
            }
        }
        return res;
    }
};
# @lc code=end