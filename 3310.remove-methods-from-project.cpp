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
        // Step 1: Build the adjacency list
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        // Step 2: Identify all suspicious methods using BFS
        vector<bool> suspicious(n, false);
        suspicious[k] = true;
        queue<int> q;
        q.push(k);

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

        // Step 3: Check if any non-suspicious method invokes a suspicious method
        bool violation = false;
        for (const auto& inv : invocations) {
            if (!suspicious[inv[0]] && suspicious[inv[1]]) {
                violation = true;
                break;
            }
        }

        // Step 4: Return results based on violation status
        vector<int> result;
        if (violation) {
            result.resize(n);
            iota(result.begin(), result.end(), 0);
        } else {
            for (int i = 0; i < n; ++i) {
                if (!suspicious[i]) {
                    result.push_back(i);
                }
            }
        }
        return result;
    }
};
# @lc code=end