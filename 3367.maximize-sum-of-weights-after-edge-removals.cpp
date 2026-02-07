#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#
# @lc code=start
class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        // Sort edges based on weights in descending order
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) { return a[2] > b[2]; });
        
        int n = edges.size() + 1;  // since there are n-1 edges for n nodes
        vector<int> parent(n), rank(n, 0), degree(n, 0);
        iota(parent.begin(), parent.end(), 0);  // Initialize parent for each node

        function<int(int)> find = [&](int u) {
            if (parent[u] != u) {
                parent[u] = find(parent[u]);  // Path compression
            }
            return parent[u];
        };

        auto unionSets = [&](int u, int v) {
            int rootU = find(u);
            int rootV = find(v);
            if (rootU != rootV) {
                if (rank[rootU] < rank[rootV]) swap(rootU, rootV);
                parent[rootV] = rootU;
                if (rank[rootU] == rank[rootV]) rank[rootU]++;
                return true;
            }
            return false;
        };

        long long maxWeight = 0;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (degree[u] < k && degree[v] < k && unionSets(u, v)) {
                maxWeight += w;
                degree[u]++;
                degree[v]++;
            }
        }
        return maxWeight;
    }
};
# @lc code=end