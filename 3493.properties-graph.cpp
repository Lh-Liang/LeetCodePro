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
        // Preprocess all properties as sets for efficient intersection
        vector<unordered_set<int>> sets(n);
        for (int i = 0; i < n; ++i) {
            sets[i] = unordered_set<int>(properties[i].begin(), properties[i].end());
        }

        // Build adjacency list
        vector<vector<int>> graph(n);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int count = 0;
                for (int val : sets[i]) {
                    if (sets[j].count(val)) ++count;
                }
                if (count >= k) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }

        // Count connected components using DFS
        vector<bool> visited(n, false);
        int components = 0;
        function<void(int)> dfs = [&](int node) {
            visited[node] = true;
            for (int nei : graph[node]) {
                if (!visited[nei]) dfs(nei);
            }
        };

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++components;
                dfs(i);
            }
        }
        // Verification step: ensure all nodes visited and components count matches expected disconnected groups
        // (for debugging or extension)
        return components;
    }
};
# @lc code=end