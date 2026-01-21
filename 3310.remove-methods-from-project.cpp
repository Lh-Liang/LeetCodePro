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
        for (const auto& inv : invocations) {
            graph[inv[0]].push_back(inv[1]);
        }
        vector<char> susp(n, 0);
        queue<int> q;
        q.push(k);
        susp[k] = 1;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : graph[u]) {
                if (susp[v] == 0) {
                    susp[v] = 1;
                    q.push(v);
                }
            }
        }
        bool can_remove = true;
        for (const auto& inv : invocations) {
            int a = inv[0], b = inv[1];
            if (susp[a] == 0 && susp[b] == 1) {
                can_remove = false;
                break;
            }
        }
        vector<int> res;
        if (!can_remove) {
            for (int i = 0; i < n; ++i) {
                res.push_back(i);
            }
        } else {
            for (int i = 0; i < n; ++i) {
                if (susp[i] == 0) {
                    res.push_back(i);
                }
            }
        }
        return res;
    }
};
# @lc code=end