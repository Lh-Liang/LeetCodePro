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
        vector<vector<int>> graph(n);
        // Build graph based on intersection condition
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (intersect(properties[i], properties[j]) >= k) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }
        // Find connected components using DFS
        vector<bool> visited(n, false);
        int components = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++components;
                dfs(i, graph, visited);
            }
        }
        return components;
    }
private:
    // Function to find the number of distinct integers common to both arrays a and b
    int intersect(const vector<int>& a, const vector<int>& b) {
        unordered_set<int> setA(a.begin(), a.end());
        int count = 0;
        for (int num : b) {
            if (setA.count(num)) { ++count; } 
        }
        return count;
    }
    // Depth First Search function to mark all reachable nodes from current node
    void dfs(int node, const vector<vector<int>>& graph, vector<bool>& visited) { 
        visited[node] = true;
        for (int neighbor : graph[node]) { 
            if (!visited[neighbor]) { dfs(neighbor, graph, visited); } 
        } 
    }
};
# @lc code=end