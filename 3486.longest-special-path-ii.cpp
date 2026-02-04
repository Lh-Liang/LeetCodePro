#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
#

# @lc code=start
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        // Step 1: Build adjacency list from edges
        unordered_map<int, vector<pair<int, int>>> adjList;
        for (const auto &edge : edges) {
            adjList[edge[0]].emplace_back(edge[1], edge[2]);
            adjList[edge[1]].emplace_back(edge[0], edge[2]);
        }

        int maxLength = 0;
        int minNodes = INT_MAX;
        unordered_set<int> globalVisited;

        // Helper function for DFS traversal
        function<void(int, int, unordered_set<int>&, bool, int)> dfs = [&](int node, int currentLength, unordered_set<int>& visitedValues, bool usedDuplicate, int nodeCount) {
            // Explore adjacent nodes
            for (const auto &[nextNode, edgeLength] : adjList[node]) {
                if (!globalVisited.count(nextNode)) { // Check global visited to prevent revisiting nodes in this tree structure
                    bool nextUsedDuplicate = usedDuplicate || visitedValues.count(nums[nextNode]);
                    if (!visitedValues.count(nums[nextNode]) || !nextUsedDuplicate) {
                        visitedValues.insert(nums[nextNode]);
                        globalVisited.insert(nextNode);
                        dfs(nextNode, currentLength + edgeLength, visitedValues, nextUsedDuplicate, nodeCount + 1);
                        visitedValues.erase(nums[nextNode]);
                        globalVisited.erase(nextNode);
                    }
                }
            }
            
            // Update results if this path is longer or has fewer nodes with same length
            if (currentLength > maxLength || (currentLength == maxLength && nodeCount < minNodes)) {
                maxLength = currentLength;
                minNodes = nodeCount;
            }
        };
        
        // Step 2-5: Start DFS traversal from the root node (node 0)
        unordered_set<int> visitedValues = {nums[0]};
        globalVisited.insert(0);
        dfs(0, 0, visitedValues, false, 1);
        
        return {maxLength, minNodes};
    }
};
# @lc code=end