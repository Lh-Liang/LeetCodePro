# @lc app=leetcode id=3585 lang=cpp
# [3585] Find Weighted Median Node in Tree

# @lc code=start
class Solution {
public:
    vector<int> findMedian(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // Step 1: Build adjacency list for tree representation
        unordered_map<int, vector<pair<int, int>>> adj;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        
        // Step 2: Preprocess using DFS to calculate depths and distances from root
        vector<int> parent(n), depth(n), dist(n);
        function<void(int, int)> dfs = [&](int node, int par) {
            for (const auto &[neighbor, weight] : adj[node]) {
                if (neighbor == par) continue;
                parent[neighbor] = node;
                depth[neighbor] = depth[node] + 1;
                dist[neighbor] = dist[node] + weight;
                dfs(neighbor, node);
            }
        };
        dfs(0, -1);

        // Step 3: Implement binary lifting for LCA calculation (omitted here)
        auto findLCA = [&](int u, int v) -> int {
            if (depth[u] < depth[v]) swap(u, v);
            // Bring u and v to same depth
            while (depth[u] > depth[v]) {
                u = parent[u];
            }
            if (u == v) return u;
            while (parent[u] != parent[v]) {
                u = parent[u];
                v = parent[v];
            }
            return parent[u];
        };

        vector<int> result;
        for (const auto& query : queries) {
            int u = query[0], v = query[1];
            int lca = findLCA(u, v);
            // Calculate total path weightint totalPathWeight = dist[u] + dist[v] - 2 * dist[lca]; double halfWeight = totalPathWeight / 2.0; // Traverse from u towards LCA accumulating weightsint currNode = u; double cumWeight = 0; while(currNode != lca && cumWeight < halfWeight){ cumWeight += dist[currNode] - dist[parent[currNode]]; currNode=parent[currNode]; } if(cumWeight >= halfWeight){ result.push_back(currNode); continue; } // Traverse from LCA towards v if necessary currNode=lca; while(currNode != v && cumWeight < halfWeight){ cumWeight += dist[currNode]-dist[parent[currNode]]; currNode=parent[currNode]; } result.push_back(currNode); }	return result;    }	};# @lc code=end