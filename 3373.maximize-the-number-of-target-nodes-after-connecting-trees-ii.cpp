#
# @lc app=leetcode id=3373 lang=cpp
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;
        vector<vector<int>> adj1(n), adj2(m);
        for (auto& e : edges1) {
            int a = e[0], b = e[1];
            adj1[a].push_back(b);
            adj1[b].push_back(a);
        }
        for (auto& e : edges2) {
            int a = e[0], b = e[1];
            adj2[a].push_back(b);
            adj2[b].push_back(a);
        }

        auto bfs_parity = [](const vector<vector<int>>& adj, int N) -> vector<int> {
            vector<int> par(N, -1);
            queue<int> q;
            q.push(0);
            par[0] = 0;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if (par[v] == -1) {
                        par[v] = par[u] ^ 1;
                        q.push(v);
                    }
                }
            }
            return par;
        };

        vector<int> par1 = bfs_parity(adj1, n);
        vector<int> cnt1(2, 0);
        for (int p : par1) cnt1[p]++;
        int sz0 = cnt1[0], sz1 = cnt1[1];

        vector<int> par2 = bfs_parity(adj2, m);
        vector<int> cnt2(2, 0);
        for (int p : par2) cnt2[p]++;
        int max2 = max(cnt2[0], cnt2[1]);

        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            int sz = (par1[i] == 0 ? sz0 : sz1);
            ans[i] = sz + max2;
        }
        return ans;
    }
};
# @lc code=end