#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].emplace_back(v, w);
            adj[v].emplace_back(u, w);
        }
        const int LOG = 18;
        vector<vector<int>> up(n, vector<int>(LOG, -1));
        vector<long long> dep(n, 0);
        vector<int> level(n, 0);
        auto dfs = [&](auto&& self, int u, int p, long long d, int lev) -> void {
            up[u][0] = p;
            dep[u] = d;
            level[u] = lev;
            for (auto [v, w] : adj[u]) {
                if (v != p) {
                    self(self, v, u, d + w, lev + 1);
                }
            }
        };
        dfs(dfs, 0, -1, 0LL, 0);
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i) {
                int anc = up[i][j - 1];
                if (anc != -1) {
                    up[i][j] = up[anc][j - 1];
                }
            }
        }
        auto get_lca = [&](int u, int v) -> int {
            if (level[u] > level[v]) std::swap(u, v);
            int diff = level[v] - level[u];
            for (int j = 0; j < LOG; ++j) {
                if ((diff >> j) & 1) {
                    v = up[v][j];
                }
            }
            if (u == v) return u;
            for (int j = LOG - 1; j >= 0; --j) {
                if (up[u][j] != up[v][j]) {
                    u = up[u][j];
                    v = up[v][j];
                }
            }
            return up[u][0];
        };
        vector<int> ans;
        for (auto& q : queries) {
            int a = q[0], b = q[1], c = q[2];
            int lab = get_lca(a, b);
            long long dab = dep[a] + dep[b] - 2LL * dep[lab];
            int lac = get_lca(a, c);
            long long dac = dep[a] + dep[c] - 2LL * dep[lac];
            int lbc = get_lca(b, c);
            long long dbc = dep[b] + dep[c] - 2LL * dep[lbc];
            long long total = dab + dac + dbc;
            ans.push_back(total / 2);
        }
        return ans;
    }
};
# @lc code=end