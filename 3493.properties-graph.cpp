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
        vector<vector<int>> adj(n);
        
        // Calculate intersections and build graph
        auto intersect = [](const vector<int>& a, const vector<int>& b) {
            unordered_set<int> setA(a.begin(), a.end());
            unordered_set<int> setB(b.begin(), b.end());
            int common = 0;
            for (int num : setA) {
                if (setB.count(num)) common++;
            }
            return common;
        };
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (intersect(properties[i], properties[j]) >= k) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        
        // Count connected components using DFS or union-find (DFS here)
        vector<bool> visited(n, false);
        function<void(int)> dfs = [&](int node) {
            visited[node] = true;
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) dfs(neighbor);