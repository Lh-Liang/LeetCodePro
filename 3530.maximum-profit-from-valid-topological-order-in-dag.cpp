#
# @lc app=leetcode id=3530 lang=cpp
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        vector<int> indegree(n, 0);
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            ++indegree[edge[1]];
        }
        queue<int> q; // Queue for Kahn's algorithm.
        vector<int> topoOrder;
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        while (!q.empty()) {
            int node = q.front(); q.pop();
            topoOrder.push_back(node);
            for (int neighbor : adj[node]) {
                if (--indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        // Use dynamic programming or greedy strategy here to maximize profit within topoOrder
        vector<pair<int, int>> nodesWithScore;
        for (int i = 0; i < n; ++i) {
            nodesWithScore.emplace_back(score[topoOrder[i]], topoOrder[i]);
        }
        sort(nodesWithScore.rbegin(), nodesWithScore.rend()); // Sort descending by score
        int maxProfit = 0;
        for (int i = 0; i < n; ++i) {
            maxProfit += nodesWithScore[i].first * (i + 1); // Calculate profit using assigned positions
        }										// Ensure optimal mapping strategy here
        return maxProfit;	// Return calculated maximum profit
    }	// Ensure dependencies are respected in calculation
};	// Add verification step if needed to confirm optimal mapping
# @lc code=end