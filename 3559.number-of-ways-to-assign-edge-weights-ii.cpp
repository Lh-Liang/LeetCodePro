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

        int LOGN = 0;
        while ((1 << LOGN) <= n) LOGN++;

        vector<int> depth(n + 1, 0);
        vector<vector<int>> up(n + 1, vector<int>(LOGN));
        vector<bool> visited(n + 1, false);
        queue<int> q;

        q.push(1);
        visited[1] = true;
        up[1][0] = 1;
        depth[1] = 0;

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

        for (int i = 1; i < LOGN; ++i) {
            for (int u = 1; u <= n; ++u) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }
        }

        auto getLCA = [&](int u, int v) {
            if (depth[u] < depth[v]) swap(u, v);
            for (int i = LOGN - 1; i >= 0; --i) {
                if (depth[u] - (1 << i) >= depth[v]) {
                    u = up[u][i];
                }
            }
            if (u == v) return u;
            for (int i = LOGN - 1; i >= 0; --i) {
                if (up[u][i] != up[v][i]) {
                    u = up[u][i];
                    v = up[v][i];
                }
            }
            return up[u][0];
        };

        vector<int> pow2(n + 1);
        pow2[0] = 1;
        const int MOD = 1e9 + 7;
        for (int i = 1; i <= n; ++i) {
            pow2[i] = (int)((1LL * pow2[i - 1] * 2) % MOD);
        }

        vector<int> results;
        results.reserve(queries.size());
        for (const auto& query : queries) {
            int u = query[0], v = query[1];
            if (u == v) {
                results.push_back(0);
                continue;
            }
            int lca = getLCA(u, v);
            int dist = depth[u] + depth[v] - 2 * depth[lca];
            results.push_back(pow2[dist - 1]);
        }

        return results;
    }
};