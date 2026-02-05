#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#
# @lc code=start
class Solution {
public:
    const int LOG = 17; // 2^17 > 1e5
    vector<vector<pair<int, int>>> adj;
    vector<vector<int>> up;
    vector<int> depth, parent;
    vector<long long> weightToRoot;
    int n;

    void dfs(int u, int p, int d, long long w) {
        parent[u] = p;
        depth[u] = d;
        weightToRoot[u] = w;
        for (auto [v, wgt] : adj[u]) {
            if (v == p) continue;
            dfs(v, u, d + 1, w + wgt);
        }
    }

    void preprocessLCA() {
        for (int i = 0; i < n; ++i) up[i][0] = parent[i];
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i) {
                if (up[i][j-1] != -1)
                    up[i][j] = up[up[i][j-1]][j-1];
            }
        }
    }

    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        for (int k = LOG - 1; k >= 0; --k) {
            if (up[u][k] != -1 && depth[up[u][k]] >= depth[v])
                u = up[u][k];
        }
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; --k) {
            if (up[u][k] != -1 && up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }
        return parent[u];
    }

    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        n = edges.size() + 1;
        adj.assign(n, {});
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].emplace_back(v, w);
            adj[v].emplace_back(u, w);
        }
        parent.assign(n, -1);
        depth.assign(n, 0);
        weightToRoot.assign(n, 0);
        up.assign(n, vector<int>(LOG, -1));
        dfs(0, -1, 0, 0);
        preprocessLCA();
        vector<int> ans;
        for (auto& q : queries) {
            int s1 = q[0], s2 = q[1], d = q[2];
            int lca1 = lca(s1, d);
            int lca2 = lca(s2, d);
            int lca12 = lca(s1, s2);
            int lcaAll = lca(lca1, lca2);
            long long total = weightToRoot[s1] + weightToRoot[s2] + weightToRoot[d]
                - weightToRoot[lca1] - weightToRoot[lca2] - weightToRoot[lca12] + weightToRoot[lcaAll];
            ans.push_back((int)total);
        }
        return ans;
    }
};
# @lc code=end