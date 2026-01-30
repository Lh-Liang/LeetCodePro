#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }

        int LOG = 0;
        while ((1 << (LOG + 1)) <= n) LOG++;
        LOG++; // Ensure enough space for lifting

        vector<int> depth(n, 0);
        vector<long long> dist_from_root(n, 0);
        vector<vector<int>> up(n, vector<int>(LOG));

        queue<int> q;
        vector<bool> visited(n, false);
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
                    depth[v] = depth[u] + 1;
                    dist_from_root[v] = dist_from_root[u] + w;
                    up[v][0] = u;
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
            if (depth[u] < depth[v]) swap(u, v);
            for (int i = LOG - 1; i >= 0; i--) {
                if (depth[u] - (1 << i) >= depth[v]) {
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

        auto get_dist = [&](int u, int v) -> long long {
            return dist_from_root[u] + dist_from_root[v] - 2 * dist_from_root[get_lca(u, v)];
        };

        vector<int> results;
        results.reserve(queries.size());
        for (const auto& query : queries) {
            int s1 = query[0], s2 = query[1], d = query[2];
            long long d12 = get_dist(s1, s2);
            long long d23 = get_dist(s2, d);
            long long d13 = get_dist(s1, d);
            // The sum of distances between three points in a tree is always even
            // result fits into int because max distance is (n-1)*10^4 = 10^9 < 2*10^9
            results.push_back((int)((d12 + d23 + d13) / 2));
        }

        return results;
    }
};
# @lc code=end