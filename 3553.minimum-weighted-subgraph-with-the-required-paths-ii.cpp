//
// @lc app=leetcode id=3553 lang=cpp
//
// [3553] Minimum Weighted Subgraph With the Required Paths II
//

// @lc code=start
class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        const int LOG = 17;
        
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        
        vector<long long> dist(n, 0);
        vector<int> dep(n, 0);
        vector<vector<int>> parent(n, vector<int>(LOG, -1));
        
        // BFS to compute dist, dep, and parent[i][0]
        queue<int> que;
        que.push(0);
        vector<bool> visited(n, false);
        visited[0] = true;
        
        while (!que.empty()) {
            int u = que.front();
            que.pop();
            for (const auto& p : adj[u]) {
                int v = p.first, w = p.second;
                if (!visited[v]) {
                    visited[v] = true;
                    dist[v] = dist[u] + w;
                    dep[v] = dep[u] + 1;
                    parent[v][0] = u;
                    que.push(v);
                }
            }
        }
        
        // Build sparse table for LCA
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                if (parent[i][j-1] != -1) {
                    parent[i][j] = parent[parent[i][j-1]][j-1];
                }
            }
        }
        
        // LCA function using binary lifting
        auto lca = [&](int u, int v) -> int {
            if (dep[u] < dep[v]) swap(u, v);
            int diff = dep[u] - dep[v];
            for (int j = 0; j < LOG; j++) {
                if ((diff >> j) & 1) {
                    u = parent[u][j];
                }
            }
            if (u == v) return u;
            for (int j = LOG - 1; j >= 0; j--) {
                if (parent[u][j] != parent[v][j]) {
                    u = parent[u][j];
                    v = parent[v][j];
                }
            }
            return parent[u][0];
        };
        
        // Distance function
        auto getDist = [&](int u, int v) -> long long {
            int l = lca(u, v);
            return dist[u] + dist[v] - 2 * dist[l];
        };
        
        vector<int> answer;
        for (const auto& q : queries) {
            int src1 = q[0], src2 = q[1], dest = q[2];
            long long d12 = getDist(src1, src2);
            long long d2d = getDist(src2, dest);
            long long d1d = getDist(src1, dest);
            // Steiner tree formula: (d12 + d2d + d1d) / 2
            answer.push_back((int)((d12 + d2d + d1d) / 2));
        }
        
        return answer;
    }
};
// @lc code=end