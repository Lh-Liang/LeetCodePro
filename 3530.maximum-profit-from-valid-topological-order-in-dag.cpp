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
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        
        // Build graph and indegree array
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }
        
        // Kahn's algorithm with priority on high score nodes
        priority_queue<pair<int, int>> pq; // (score, node)
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) pq.push({score[i], i});
        }
        
        vector<int> topoOrder;
        while (!pq.empty()) {
            int node = pq.top().second; pq.pop();
            topoOrder.push_back(node);
            for (int neighbor : graph[node]) {
                if (--indegree[neighbor] == 0) pq.push({score[neighbor], neighbor});
            }
        }

        // Calculate maximum profit based on topological order
        int maxProfit = 0;
        for (int i = 0; i < n; ++i) {
            maxProfit += score[topoOrder[i]] * (i + 1);
        }

        return maxProfit;
    }
};
# @lc code=end