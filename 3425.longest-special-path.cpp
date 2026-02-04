/*
 * @lc app=leetcode id=3425 lang=cpp
 *
 * [3425] Longest Special Path
 */

#include <vector>
#include <unordered_set>
#include <functional>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].emplace_back(edge[1], edge[2]);
            adj[edge[1]].emplace_back(edge[0], edge[2]);
        }
        int maxLength = 0;
        int minNodes = n;
        function<void(int, int, int, unordered_set<int>&)> dfs = [&](int node, int length, int nodesCount, unordered_set<int>& visited) {
            if (length > maxLength) { 
                maxLength = length; 
                minNodes = nodesCount; 
            } else if (length == maxLength) { 
                minNodes = min(minNodes, nodesCount); 
            } 
            for (auto& [neighbor, weight] : adj[node]) { 
                if (visited.find(nums[neighbor]) == visited.end()) { 
                    visited.insert(nums[neighbor]); 
                    dfs(neighbor, length + weight, nodesCount + 1, visited); 
                    visited.erase(nums[neighbor]); 
                } 
            } 
        };
        for (int i = 0; i < n; ++i) { 
            unordered_set<int> visited; 
            visited.insert(nums[i]); 
            dfs(i, 0, 1, visited); 
        }
        return {maxLength, minNodes};
    }
};
// @lc code=end