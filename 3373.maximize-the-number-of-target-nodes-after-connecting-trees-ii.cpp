#
# @lc app=leetcode id=3373 lang=cpp
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1, m = edges2.size() + 1;
        vector<vector<int>> g1(n), g2(m);
        for (auto& e : edges1) {
            g1[e[0]].push_back(e[1]);
            g1[e[1]].push_back(e[0]);
        }
        for (auto& e : edges2) {
            g2[e[0]].push_back(e[1]);
            g2[e[1]].push_back(e[0]);
        }
        vector<int> parity1(n, -1), parity2(m, -1);
        // BFS for tree1
        queue<int> q;
        q.push(0); parity1[0] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g1[u]) {
                if (parity1[v] == -1) {
                    parity1[v] = parity1[u] ^ 1;
                    q.push(v);
                }
            }
        }
        // BFS for tree2
        q.push(0); parity2[0] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g2[u]) {
                if (parity2[v] == -1) {
                    parity2[v] = parity2[u] ^ 1;
                    q.push(v);
                }
            }
        }
        int cnt1[2] = {0, 0}, cnt2[2] = {0, 0};
        for (int x : parity1) cnt1[x]++;
        for (int x : parity2) cnt2[x]++;
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            int p = parity1[i];
            ans[i] = cnt1[p] + max(cnt2[0], cnt2[1]);
        }
        return ans;
    }
};
# @lc code=end