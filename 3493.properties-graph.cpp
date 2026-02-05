#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#
# @lc code=start
class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        // Precompute sets for each property array
        vector<unordered_set<int>> sets(n);
        for (int i = 0; i < n; ++i) {
            for (int num : properties[i]) {
                sets[i].insert(num);
            }
        }
        // Build adjacency list
        vector<vector<int>> adj(n);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int cnt = 0;
                for (int num : sets[i]) {
                    if (sets[j].count(num)) ++cnt;
                }
                if (cnt >= k) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        // DFS to count components
        vector<bool> visited(n, false);
        int components = 0;
        function<void(int)> dfs = [&](int u) {
            visited[u] = true;
            for (int v : adj[u]) {
                if (!visited[v]) dfs(v);
            }
        };
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++components;
                dfs(i);
            }
        }
        return components;
    }
};
# @lc code=end