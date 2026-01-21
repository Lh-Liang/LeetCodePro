#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3367 lang=cpp
 *
 * [3367] Maximize Sum of Weights after Edge Removals
 */

// @lc code=start
class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = (int)edges.size() + 1;
        vector<vector<pair<int,int>>> g(n);
        g.assign(n, {});
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }

        // Build parent and traversal order iteratively
        vector<int> parent(n, -1);
        vector<int> order;
        order.reserve(n);
        stack<int> st;
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top();
            st.pop();
            order.push_back(u);
            for (auto [v, w] : g[u]) {
                if (parent[v] != -1) continue;
                parent[v] = u;
                st.push(v);
            }
        }

        vector<long long> f0(n, 0), f1(n, 0);
        int cap1 = max(0, k - 1);

        // Postorder DP
        for (int idx = n - 1; idx >= 0; --idx) {
            int u = order[idx];
            long long base = 0;
            vector<long long> gains;
            gains.reserve(g[u].size());

            for (auto [v, w] : g[u]) {
                if (v == parent[u]) continue;
                base += f0[v];
                long long gain = (long long)w + f1[v] - f0[v];
                if (gain > 0) gains.push_back(gain);
            }

            sort(gains.begin(), gains.end(), greater<long long>());

            // prefix sums of sorted gains
            long long sum0 = 0, sum1 = 0;
            int m = (int)gains.size();
            int take0 = min(k, m);
            int take1 = min(cap1, m);
            for (int i = 0; i < take0; ++i) sum0 += gains[i];
            for (int i = 0; i < take1; ++i) sum1 += gains[i];

            f0[u] = base + sum0;
            f1[u] = base + sum1;
        }

        return f0[0];
    }
};
// @lc code=end
