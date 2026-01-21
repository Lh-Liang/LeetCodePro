#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3559 lang=cpp
 *
 * [3559] Number of Ways to Assign Edge Weights II
 */

// @lc code=start
class Solution {
public:
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        const int MOD = 1'000'000'007;
        int n = (int)edges.size() + 1;

        vector<vector<int>> g(n + 1);
        g.reserve(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }

        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        vector<vector<int>> up(LOG, vector<int>(n + 1, 0));
        vector<int> depth(n + 1, 0);

        // Iterative DFS from root=1 to fill depth and up[0]
        vector<int> parent(n + 1, 0);
        stack<int> st;
        st.push(1);
        parent[1] = 0;
        depth[1] = 0;

        while (!st.empty()) {
            int v = st.top();
            st.pop();
            up[0][v] = parent[v];
            for (int nei : g[v]) {
                if (nei == parent[v]) continue;
                parent[nei] = v;
                depth[nei] = depth[v] + 1;
                st.push(nei);
            }
        }

        // Build binary lifting table
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) {
                int mid = up[k - 1][v];
                up[k][v] = mid ? up[k - 1][mid] : 0;
            }
        }

        auto lca = [&](int a, int b) {
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

        // Precompute powers of 2
        vector<int> pow2(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            pow2[i] = (int)((2LL * pow2[i - 1]) % MOD);
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int u = q[0], v = q[1];
            int w = lca(u, v);
            int L = depth[u] + depth[v] - 2 * depth[w]; // number of edges on path
            if (L == 0) ans.push_back(0);
            else ans.push_back(pow2[L - 1]);
        }
        return ans;
    }
};
// @lc code=end
