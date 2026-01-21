#
# @lc app=leetcode id=3559 lang=cpp
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution {
public:
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        const int MOD = 1000000007;
        const int LOG = 18;
        vector<vector<int>> parent(LOG, vector<int>(n + 1, 0));
        vector<int> depth(n + 1, 0);
        // BFS to compute depth and parent[0]
        queue<int> q;
        vector<bool> vis(n + 1, false);
        q.push(1);
        vis[1] = true;
        depth[1] = 0;
        parent[0][1] = 0;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            for (int nei : adj[node]) {
                if (!vis[nei]) {
                    vis[nei] = true;
                    parent[0][nei] = node;
                    depth[nei] = depth[node] + 1;
                    q.push(nei);
                }
            }
        }
        // Build parent table
        for (int j = 1; j < LOG; j++) {
            for (int i = 1; i <= n; i++) {
                int anc = parent[j - 1][i];
                parent[j][i] = (anc ? parent[j - 1][anc] : 0);
            }
        }
        // Precompute 2^i % MOD
        vector<long long> pow2(n, 1LL);
        for (int i = 1; i < n; i++) {
            pow2[i] = pow2[i - 1] * 2LL % MOD;
        }
        // LCA lambda
        auto getLCA = [&](int x, int y) -> int {
            int u = x, v = y;
            if (depth[u] > depth[v]) std::swap(u, v);
            int diff = depth[v] - depth[u];
            for (int j = 0; j < LOG; j++) {
                if ((diff >> j) & 1) {
                    v = parent[j][v];
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
        vector<int> answer;
        for (auto& query : queries) {
            int u = query[0], v = query[1];
            if (u == v) {
                answer.push_back(0);
                continue;
            }
            int lca = getLCA(u, v);
            int k = depth[u] + depth[v] - 2 * depth[lca];
            long long ways = pow2[k - 1];
            answer.push_back(ways % MOD);
        }
        return answer;
    }
};
# @lc code=end