//
// @lc app=leetcode id=3559 lang=cpp
//
// [3559] Number of Ways to Assign Edge Weights II
//

// @lc code=start
class Solution {
public:
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        const int MOD = 1e9 + 7;
        const int LOG = 18;
        
        // Build adjacency list
        vector<vector<int>> adj(n + 1);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        // BFS to compute depth and immediate parent
        vector<int> depth(n + 1, -1);
        vector<vector<int>> parent(LOG, vector<int>(n + 1, 0));
        
        queue<int> bfsQ;
        bfsQ.push(1);
        depth[1] = 0;
        parent[0][1] = 1; // root's parent is itself
        
        while (!bfsQ.empty()) {
            int u = bfsQ.front();
            bfsQ.pop();
            for (int v : adj[u]) {
                if (depth[v] == -1) {
                    depth[v] = depth[u] + 1;
                    parent[0][v] = u;
                    bfsQ.push(v);
                }
            }
        }
        
        // Build binary lifting table
        for (int j = 1; j < LOG; j++) {
            for (int i = 1; i <= n; i++) {
                parent[j][i] = parent[j-1][parent[j-1][i]];
            }
        }
        
        // LCA function using binary lifting
        auto lca = [&](int u, int v) -> int {
            if (depth[u] < depth[v]) swap(u, v);
            int diff = depth[u] - depth[v];
            for (int j = 0; j < LOG; j++) {
                if ((diff >> j) & 1) {
                    u = parent[j][u];
                }
            }
            if (u == v) return u;
            for (int j = LOG - 1; j >= 0; j--) {
                if (parent[j][u] != parent[j][v]) {
                    u = parent[j][u];
                    v = parent[j][v];
                }
            }
            return parent[0][u];
        };
        
        // Precompute powers of 2
        vector<long long> pow2(n + 1);
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow2[i] = (pow2[i-1] * 2) % MOD;
        }
        
        // Process queries
        vector<int> result;
        for (auto& q : queries) {
            int u = q[0], v = q[1];
            int l = lca(u, v);
            int pathLen = depth[u] + depth[v] - 2 * depth[l];
            if (pathLen == 0) {
                result.push_back(0);
            } else {
                result.push_back((int)pow2[pathLen - 1]);
            }
        }
        
        return result;
    }
};
// @lc code=end