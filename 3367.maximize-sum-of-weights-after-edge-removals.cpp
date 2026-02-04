#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        // Sort edges by weight in descending order.
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) { return a[2] > b[2]; });
        unordered_map<int, int> degree; // To track degree of each node.
        vector<int> parent(edges.size() + 1), rank(edges.size() + 1, 0);
        iota(parent.begin(), parent.end(), 0); // Initialize union-find structure.
        
        function<int(int)> find = [&](int u) {
            if (parent[u] != u) parent[u] = find(parent[u]);
            return parent[u];
        };
        
        auto union_sets = [&](int u, int v) {
            u = find(u);
            v = find(v);
            if (u != v) {
                if (rank[u] < rank[v]) swap(u, v);
                parent[v] = u;
                if (rank[u] == rank[v]) rank[u]++;
            }
        };

        long long maxSum = 0;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (degree[u] < k && degree[v] < k && find(u) != find(v)) { // Check constraints and connectivity before adding edge.
                maxSum += w;
                degree[u]++;
                degree[v]++;
                union_sets(u, v);
            }
        }
        return maxSum;
    }
};
# @lc code=end