#
# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution {
public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        // Build adjacency list
        vector<vector<int>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        int maxLen = 1; // At least one node is always a palindrome
        // Helper DFS function
        function<void(int, vector<int>&, int)> dfs = [&](int u, vector<int>& path, int visited) {
            // Check palindrome
            int sz = path.size();
            bool isPal = true;
            for (int i = 0; i < sz / 2; ++i) {
                if (label[path[i]] != label[path[sz - 1 - i]]) {
                    isPal = false;
                    break;
                }
            }
            if (isPal) {
                maxLen = max(maxLen, sz);
            }
            // Try extending path
            for (int v : adj[u]) {
                if (!(visited & (1 << v))) {
                    path.push_back(v);
                    dfs(v, path, visited | (1 << v));
                    path.pop_back();
                }
            }
        };
        // Try starting from every node
        for (int i = 0; i < n; ++i) {
            vector<int> path = {i};
            dfs(i, path, 1 << i);
        }
        return maxLen;
    }
};
# @lc code=end