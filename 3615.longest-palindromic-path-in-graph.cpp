# @lc app=leetcode id=3615 lang=cpp

# [3615] Longest Palindromic Path in Graph

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
        // Step 1: Build graph adjacency list
        vector<unordered_set<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }
        
        int maxLength = 0;
        unordered_map<int, unordered_map<int, int>> memo;
        
        // Step 2 & 3: Define DFS function with character tracking and palindrome checking
        function<int(int, int, vector<int>&)> dfs = [&](int node, int mask, vector<int>& charCount) {
            if (memo[node].count(mask)) return memo[node][mask];
            
            charCount[label[node] - 'a']++; // Increment character count for current node
            int oddCount = 0;
            for (int count : charCount) {
                if (count % 2 == 1) oddCount++;
            }
            
            int length = (oddCount <= 1) ? __builtin_popcount(mask) : 0; // Check if current path can be a palindrome and calculate its length
            
            for (int neighbor : graph[node]) {
                if (!(mask & (1 << neighbor))) { // Check if neighbor is unvisited in current path
                    int newMask = mask | (1 << neighbor);
                    length = max(length, dfs(neighbor, newMask, charCount));
                }
            }
            
            charCount[label[node] - 'a']--; // Decrement character count backtrack cleanup
            return memo[node][mask] = length;
        };

        // Step 4 & 5: Explore each node as start point and find longest palindromic path
        for (int i = 0; i < n; ++i) {
            vector<int> charCount(26, 0); // Reset character counts for each start node
            maxLength = max(maxLength, dfs(i, 1 << i, charCount));
        }
        
        return maxLength;
    }
};
# @lc code=end