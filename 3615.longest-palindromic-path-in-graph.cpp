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
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        int maxLength = 1;
        
        // Try all starting nodes
        for (int start = 0; start < n; start++) {
            string path = "";
            path += label[start];
            dfs(start, adj, label, 1 << start, path, maxLength);
        }
        
        return maxLength;
    }
    
    void dfs(int node, vector<vector<int>>& adj, string& label, 
             int visited, string& path, int& maxLength) {
        // Check if current path is palindrome
        if (isPalindrome(path)) {
            maxLength = max(maxLength, (int)path.size());
        }
        
        // Try to extend the path
        for (int next : adj[node]) {
            if (!(visited & (1 << next))) {
                path += label[next];
                dfs(next, adj, label, visited | (1 << next), path, maxLength);
                path.pop_back();
            }
        }
    }
    
    bool isPalindrome(const string& s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }
};
# @lc code=end