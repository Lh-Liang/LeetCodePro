# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#
# @lc code=start
class Solution {
public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        unordered_map<int, vector<int>> graph;
        // Build the graph from edges
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        int maxLength = 0;
        // Start DFS from each node
        for (int i = 0; i < n; ++i) {
            vector<bool> visited(n, false);
            dfs(graph, label, i, "", visited, maxLength);
        }
        return maxLength;
    }
private:
    void dfs(unordered_map<int, vector<int>>& graph, const string& label, int node, string currentPath, vector<bool>& visited, int& maxLength) {
        visited[node] = true;
        currentPath += label[node];
        // Check if currentPath is a palindrome and update maxLength if needed
        if (isPalindrome(currentPath)) {
            maxLength = max(maxLength, (int)currentPath.length());
        }
        // Explore neighbors recursively if not already visited
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(graph, label, neighbor, currentPath, visited, maxLength);
            }
        }
        visited[node] = false; // Backtrack step for other potential paths. "}"