#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        int LOG = 18;
        vector<vector<int>> up(n, vector<int>(LOG));
        vector<long long> depth(n, 0);
        vector<int> level(n, 0);
        vector<bool> visited(n, false);

        queue<int> q;
        q.push(0);
        visited[0] = true;
        up[0][0] = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (!visited[v]) {
                    visited[v] = true;
                    up[v][0] = u;
                    depth[v] = depth[u] + w;
                    level[v] = level[u] + 1;
                    q.push(v);
                }
            }
        }

        for (int i = 1; i < LOG; i++) {
            for (int u = 0; u < n; u++) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }
        }

        auto get_lca = [&](int u, int v) {
            if (level[u] < level[v]) swap(u, v);
            for (int i = LOG - 1; i >= 0; i--) {
                if (level[u] - (1 << i) >= level[v]) {
                    u = up[u][i];
                }
            }
            if (u == v) return u;
            for (int i = LOG - 1; i >= 0; i--) {
                if (up[u][i] != up[v][i]) {
                    u = up[u][i];
                    v = up[v][i];
                }
            }
            return up[u][0];
        };

        auto get_dist = [&](int u, int v) {
            return depth[u] + depth[v] - 2 * depth[get_lca(u, v)];
        };

        vector<long long> results;
        results.reserve(queries.size());
        for (const auto& query : queries) {
            int a = query[0];
            int b = query[1];
            int c = query[2];
            long long d_ab = get_dist(a, b);
            long long d_bc = get_dist(b, c);
            long long d_ca = get_dist(c, a);
            results.push_back((d_ab + d_bc + d_ca) / 2);
        }

        return results;
    }
};
# @lc code=end