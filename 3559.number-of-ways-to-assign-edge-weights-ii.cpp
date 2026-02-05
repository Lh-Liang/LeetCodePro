#
# @lc app=leetcode id=3559 lang=cpp
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution {
public:
    const int MOD = 1e9 + 7;
    int n;
    vector<vector<int>> adj;
    vector<vector<int>> up;
    vector<int> depth;
    int LOG;
    
    void dfs(int v, int p) {
        up[v][0] = p;
        for (int i = 1; i <= LOG; ++i) {
            if (up[v][i-1] != -1)
                up[v][i] = up[up[v][i-1]][i-1];
        }
        for (int u : adj[v]) {
            if (u != p) {
                depth[u] = depth[v] + 1;
                dfs(u, v);
            }
        }
    }
    
    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        for (int i = LOG; i >= 0; --i) {
            if (up[u][i] != -1 && depth[up[u][i]] >= depth[v])
                u = up[u][i];
        }
        if (u == v) return u;
        for (int i = LOG; i >= 0; --i) {
            if (up[u][i] != -1 && up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }
    
    int modpow(int a, int b, int m) {
        int res = 1;
        while (b) {
            if (b & 1) res = (1LL * res * a) % m;
            a = (1LL * a * a) % m;
            b >>= 1;
        }
        return res;
    }
    
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        n = edges.size() + 1;
        LOG = 0;
        while ((1 << LOG) <= n) ++LOG;
        adj.assign(n + 1, vector<int>());
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        up.assign(n + 1, vector<int>(LOG + 1, -1));
        depth.assign(n + 1, 0);
        dfs(1, -1);
        vector<int> res;
        for (auto& q : queries) {
            int u = q[0], v = q[1];
            if (u == v) {
                res.push_back(0);
                continue;
            }
            int anc = lca(u, v);
            int L = depth[u] + depth[v] - 2 * depth[anc];
            res.push_back(modpow(2, L-1, MOD));
        }
        return res;
    }
};
# @lc code=end