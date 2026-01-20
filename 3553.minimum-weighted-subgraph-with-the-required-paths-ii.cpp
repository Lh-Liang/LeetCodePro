#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
class Solution {
public:
    // Using long long for distances to prevent overflow given constraints.
    // Note: The template provided in the prompt had vector<int>, but constraints
    // imply results can exceed 2^31 - 1. Standard LeetCode usually uses vector<long long>
    // for such problems. I will use vector<long long> for correctness.
    vector<long long> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        // Binary Lifting Preprocessing
        // up[u][i] is the 2^i-th ancestor of u
        int LOG = 20;
        vector<vector<int>> up(n, vector<int>(LOG, 0));
        vector<int> depth_nodes(n, 0); // depth in terms of number of edges (level)
        vector<long long> dist_root(n, 0); // weighted distance from root

        // DFS to build tree structure rooted at 0
        // Using iterative DFS to avoid stack overflow on deep trees (N=10^5)
        vector<int> parent(n, -1);
        vector<int> stack;
        stack.push_back(0);
        parent[0] = 0; // Root's parent is itself for logic consistency or handle separately
        
        // Standard BFS or iterative DFS to populate levels and parents
        // BFS is safer for depth calculation logic order
        vector<bool> visited(n, false);
        vector<int> q;
        q.reserve(n);
        q.push_back(0);
        visited[0] = true;
        
        int head = 0;
        while(head < q.size()){
            int u = q[head++];
            // Precompute binary lifting for u
            if (u != 0) {
                up[u][0] = parent[u];
                for (int i = 1; i < LOG; i++) {
                    up[u][i] = up[up[u][i-1]][i-1];
                }
            } else {
                for (int i = 0; i < LOG; i++) up[u][i] = 0;
            }
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (!visited[v]) {
                    visited[v] = true;
                    parent[v] = u;
                    depth_nodes[v] = depth_nodes[u] + 1;
                    dist_root[v] = dist_root[u] + w;
                    q.push_back(v);
                }
            }
        }

        auto get_lca = [&](int u, int v) -> int {
            if (depth_nodes[u] < depth_nodes[v]) swap(u, v);
            
            // Lift u to same depth as v
            for (int i = LOG - 1; i >= 0; i--) {
                if (depth_nodes[u] - (1 << i) >= depth_nodes[v]) {
                    u = up[u][i];
                }
            }
            
            if (u == v) return u;
            
            // Lift both
            for (int i = LOG - 1; i >= 0; i--) {
                if (up[u][i] != up[v][i]) {
                    u = up[u][i];
                    v = up[v][i];
                }
            }
            return up[u][0];
        };

        auto get_dist = [&](int u, int v) -> long long {
            int lca = get_lca(u, v);
            return dist_root[u] + dist_root[v] - 2 * dist_root[lca];
        };

        vector<long long> results;
        results.reserve(queries.size());
        for (const auto& query : queries) {
            int src1 = query[0];
            int src2 = query[1];
            int dest = query[2];
            
            long long d1 = get_dist(src1, src2);
            long long d2 = get_dist(src1, dest);
            long long d3 = get_dist(src2, dest);
            
            // The size of the subtree connecting u, v, w is (dist(u,v) + dist(v,w) + dist(u,w)) / 2
            results.push_back((d1 + d2 + d3) / 2);
        }

        return results;
    }
};
# @lc code=end