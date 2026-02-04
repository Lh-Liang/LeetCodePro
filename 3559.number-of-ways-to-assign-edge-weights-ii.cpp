#
# @lc app=leetcode id=3559 lang=cpp
#
# [3559] Number of Ways to Assign Edge Weights II
#
# @lc code=start
class Solution {
public:
    static constexpr int MOD = 1e9 + 7;
    int n;
    vector<vector<int>> tree;
    vector<int> depth;
    vector<vector<int>> up;
    int LOG;

    void dfs(int u, int p) {
        up[u][0] = p;
        for (int i = 1; i <= LOG; ++i) {
            if (up[u][i-1] != -1)
                up[u][i] = up[up[u][i-1]][i-1];
        }
        for (int v : tree[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
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

    int fastPow(int a, int b) {
        int res = 1;
        while (b) {
            if (b & 1) res = 1LL * res * a % MOD;
            a = 1LL * a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        n = edges.size() + 1;
        tree.resize(n + 1);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            tree[u].push_back(v);
            tree[v].push_back(u);
        }
        LOG = 0;
        while ((1 << LOG) <= n) LOG++;
        up.assign(n + 1, vector<int>(LOG + 1, -1));
        depth.assign(n + 1, 0);
        dfs(1, -1);
        vector<int> answer;
        for (auto& q : queries) {
            int u = q[0], v = q[1];
            if (u == v) {
                answer.push_back(0);
                continue;
            }
            int ancestor = lca(u, v);
            int k = depth[u] + depth[v] - 2 * depth[ancestor];
            int ways = fastPow(2, k - 1);
            answer.push_back(ways);
        }
        return answer;
    }
};
# @lc code=end