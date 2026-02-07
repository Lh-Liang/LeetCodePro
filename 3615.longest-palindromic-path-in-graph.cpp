#
# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#
# @lc code=start
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <functional>
using namespace std;

class Solution {
public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        // Step 1: Build adjacency list for the graph
        unordered_map<int, vector<int>> adjList;
        for (const auto& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        
        // Step 2: Initialize variables for tracking max palindrome length
        int maxLength = 1; // At least one node is always a palindrome of length 1 by itself.
        
        // Helper function to check if a string is a palindrome incrementally
        auto isIncrementalPalindrome = [](const string& s) -> bool {
            int left = 0, right = s.size() - 1;
            while (left < right) {
                if (s[left] != s[right]) return false;
                ++left; --right;
            }
            return true;
        };
        
        // Step 3: DFS Helper Function Definition
        function<void(int, string&, unordered_set<int>&)> dfs = [&](int node, string& currentPath, unordered_set<int>& visited) {
            visited.insert(node);
            currentPath.push_back(label[node]);
            
            // Check if currentPath is a palindrome incrementally and update maxLength if so
            if (isIncrementalPalindrome(currentPath)) {
                maxLength = max(maxLength, (int)currentPath.size());
            }
            
            // Explore neighbors
            for (int neighbor : adjList[node]) {
                if (!visited.count(neighbor)) {					dfs(neighbor, currentPath, visited);			}
		}

	// Backtrack step
	visited.erase(node);
	currentPath.pop_back();
};
    	// Step 4: Start DFS from each node since any node can be a starting point for a path.
    for (int i = 0; i < n; ++i) { 
        unordered_set<int> visited; 	string currentPath; 	dfs(i, currentPath,	visited); 	} 	return maxLength; 	} ; # @lc code=end