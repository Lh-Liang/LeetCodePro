#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#
# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> adj(n);
        adj.reserve(n);
        for (auto &e : invocations) {
            adj[e[0]].push_back(e[1]);
        }

        // Step 1: find all suspicious methods reachable from k
        vector<char> suspicious(n, 0);
        deque<int> dq;
        dq.push_back(k);
        suspicious[k] = 1;
        while (!dq.empty()) {
            int u = dq.front();
            dq.pop_front();
            for (int v : adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = 1;
                    dq.push_back(v);
                }
            }
        }

        // Step 2: check if any outside method invokes inside suspicious set
        for (auto &e : invocations) {
            int a = e[0], b = e[1];
            if (suspicious[b] && !suspicious[a]) {
                // cannot remove all suspicious methods
                vector<int> all;
                all.reserve(n);
                for (int i = 0; i < n; ++i) all.push_back(i);
                return all;
            }
        }

        // Step 3: remove all suspicious methods
        vector<int> remain;
        remain.reserve(n);
        for (int i = 0; i < n; ++i) {
            if (!suspicious[i]) remain.push_back(i);
        }
        return remain;
    }
};
# @lc code=end
