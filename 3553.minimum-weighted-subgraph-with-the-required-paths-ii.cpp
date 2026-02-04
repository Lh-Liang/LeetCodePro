#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    static const int LOG = 17; // 2^17 > 1e5
    vector<vector<pair<int, int>>> adj;
    vector<vector<int>> up; // up[v][i]: the 2^i-th ancestor of v
    vector<int> depth, tin, tout;
    vector<long long> weightFromRoot;
    int timer = 0, n;

    void dfs(int v, int p, int d, long long w) {
        tin[v] = ++timer;
        up[v][0] = p;
        depth[v] = d;
        weightFromRoot[v] = w;
        for (int i = 1; i < LOG; ++i) {
            up[v][i] = up[up[v][i-1]][i-1];
        }
        for (auto& [to, wt] : adj[v]) {
            if (to != p) {
                dfs(to, v, d+1, w+wt);
            }
        }
        tout[v] = ++timer;
    }

    bool isAncestor(int u, int v) {
        return tin[u] <= tin[v] && tout[u] >= tout[v];
    }

    int lca(int u, int v) {
        if (isAncestor(u, v)) return u;
        if (isAncestor(v, u)) return v;
        for (int i = LOG-1; i >= 0; --i) {
            if (!isAncestor(up[u][i], v)) {
                u = up[u][i];
            }
        }
        return up[u][0];
    }

    long long pathWeight(int u, int v) {
        int a = lca(u, v);
        return weightFromRoot[u] + weightFromRoot[v] - 2 * weightFromRoot[a];
    }

    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        n = edges.size() + 1;
        adj.assign(n, {});
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        up.assign(n, vector<int>(LOG));
        depth.assign(n, 0);
        tin.assign(n, 0);
        tout.assign(n, 0);
        weightFromRoot.assign(n, 0);
        timer = 0;
        dfs(0, 0, 0, 0);
        vector<int> ans;
        for (auto& q : queries) {
            int s1 = q[0], s2 = q[1], d = q[2];
            int l1 = lca(s1, d);
            int l2 = lca(s2, d);
            int l3 = lca(s1, s2);
            int l = lca(l1, l2); // LCA of all three nodes
            // Calculate the total weight ensuring no double-counting
            long long res = weightFromRoot[s1] + weightFromRoot[s2] + weightFromRoot[d] - weightFromRoot[l1] - weightFromRoot[l2] - weightFromRoot[l3];
            // Verification: the result is the sum of unique edges in the union of the paths
            ans.push_back((int)res);
        }
        return ans;
    }
};
# @lc code=end