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
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

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

        bool canRemove = true;
        for (const auto& inv : invocations) {
            // Check if a method outside the group invokes a method within it
            if (!isSuspicious[inv[0]] && isSuspicious[inv[1]]) {
                canRemove = false;
                break;
            }
        }

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