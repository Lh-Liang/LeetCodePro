#
# @lc app=leetcode id=3559 lang=cpp
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        vector<int> depth(n + 1, 0);
        vector<vector<int>> up(n + 1, vector<int>(18, 0));
        vector<bool> visited(n + 1, false);
        queue<int> q;

        q.push(1);
        visited[1] = true;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    up[v][0] = u;
                    q.push(v);
                }
            }
        }

        for (int j = 1; j < 18; ++j) {
            for (int i = 1; i <= n; ++i) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }

        auto get_lca = [&](int u, int v) {
            if (depth[u] < depth[v]) swap(u, v);
            for (int j = 17; j >= 0; --j) {
                if (depth[u] - (1 << j) >= depth[v]) {
                    u = up[u][j];
                }
            }
            if (u == v) return u;
            for (int j = 17; j >= 0; --j) {
                if (up[u][j] != up[v][j]) {
                    u = up[u][j];
                    v = up[v][j];
                }
            }
            return up[u][0];
        };

        vector<int> pow2(n + 1);
        const int MOD = 1000000007;
        pow2[0] = 1;
        for (int i = 1; i <= n; ++i) {
            pow2[i] = (pow2[i - 1] * 2LL) % MOD;
        }

        int m = queries.size();
        vector<int> results(m);
        for (int i = 0; i < m; ++i) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                results[i] = 0;
            } else {
                int lca = get_lca(u, v);
                int dist = depth[u] + depth[v] - 2 * depth[lca];
                results[i] = pow2[dist - 1];
            }
        }

        return results;
    }
};
# @lc code=end