#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3373 lang=cpp
//
// [3373] Maximize the Number of Target Nodes After Connecting Trees II
//

// @lc code=start
class Solution {
    pair<vector<int>, array<int,2>> colorAndCount(int N, const vector<vector<int>>& edges) {
        vector<vector<int>> g(N);
        g.reserve(N);
        for (auto &e : edges) {
            int a = e[0], b = e[1];
            g[a].push_back(b);
            g[b].push_back(a);
        }

        vector<int> col(N, -1);
        queue<int> q;
        col[0] = 0;
        q.push(0);
        array<int,2> cnt{0,0};
        cnt[0]++;

        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g[u]) {
                if (col[v] == -1) {
                    col[v] = col[u] ^ 1;
                    cnt[col[v]]++;
                    q.push(v);
                }
            }
        }
        return {col, cnt};
    }

public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;

        auto [col1, cnt1] = colorAndCount(n, edges1);
        auto [col2, cnt2] = colorAndCount(m, edges2);

        int best2 = max(cnt2[0], cnt2[1]);
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            ans[i] = cnt1[col1[i]] + best2;
        }
        return ans;
    }
};
// @lc code=end
