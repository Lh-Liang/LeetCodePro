#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#

# @lc code=start
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        vector<bool> is_suspicious(n, false);
        queue<int> q;
        
        is_suspicious[k] = true;
        q.push(k);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!is_suspicious[v]) {
                    is_suspicious[v] = true;
                    q.push(v);
                }
            }
        }

        bool can_remove = true;
        for (const auto& inv : invocations) {
            if (!is_suspicious[inv[0]] && is_suspicious[inv[1]]) {
                can_remove = false;
                break;
            }
        }

        vector<int> result;
        if (can_remove) {
            for (int i = 0; i < n; ++i) {
                if (!is_suspicious[i]) {
                    result.push_back(i);
                }
            }
        } else {
            result.resize(n);
            iota(result.begin(), result.end(), 0);
        }

        return result;
    }
};
# @lc code=end