#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3553 lang=cpp
 *
 * [3553] Minimum Weighted Subgraph With the Required Paths II
 */

// @lc code=start
class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = (int)edges.size() + 1;
        vector<vector<pair<int,int>>> g(n);
        g.reserve(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }

        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;

        vector<int> depth(n, 0), parent(n, 0);
        vector<long long> distRoot(n, 0);

        // Iterative DFS to compute parent, depth, distRoot
        vector<int> st;
        st.reserve(n);
        st.push_back(0);
        parent[0] = 0;
        depth[0] = 0;
        distRoot[0] = 0;

        // Need an explicit stack with iterator via parent check
        // We'll do classic stack of (u, p)
        vector<pair<int,int>> stack2;
        stack2.reserve(n);
        stack2.push_back({0, 0});

        while (!stack2.empty()) {
            auto [u, p] = stack2.back();
            stack2.pop_back();
            parent[u] = p;
            for (auto [v, w] : g[u]) {
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                distRoot[v] = distRoot[u] + (long long)w;
                stack2.push_back({v, u});
            }
        }

        vector<vector<int>> up(LOG, vector<int>(n, 0));
        for (int i = 0; i < n; i++) up[0][i] = parent[i];
        for (int k = 1; k < LOG; k++) {
            for (int i = 0; i < n; i++) {
                up[k][i] = up[k-1][ up[k-1][i] ];
            }
        }

        auto lca = [&](int a, int b) -> int {
            if (depth[a] < depth[b]) swap(a, b);
            int diff = depth[a] - depth[b];
            for (int k = 0; k < LOG; k++) {
                if (diff & (1 << k)) a = up[k][a];
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; k--) {
                if (up[k][a] != up[k][b]) {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            return up[0][a];
        };

        auto dist = [&](int a, int b) -> long long {
            int c = lca(a, b);
            return distRoot[a] + distRoot[b] - 2LL * distRoot[c];
        };

        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int a = q[0], b = q[1], c = q[2];
            long long dab = dist(a, b);
            long long dbc = dist(b, c);
            long long dca = dist(c, a);
            long long res = (dab + dbc + dca) / 2LL;
            ans.push_back((int)res);
        }
        return ans;
    }
};
// @lc code=end
