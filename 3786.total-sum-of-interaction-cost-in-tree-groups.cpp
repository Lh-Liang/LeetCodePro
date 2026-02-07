# @lc app=leetcode id=3786 lang=cpp
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        long long totalCost = 0;
        vector<bool> visited(n, false);
        
        function<pair<long long, int>(int, int)> dfs = [&](int node, int g) -> pair<long long, int> {
            visited[node] = true;
            long long subtreeCost = 0;
            int subtreeSize = 1;
            for (int neighbor : adj[node]) {
                if (!visited[neighbor] && group[neighbor] == g) {
                    auto [childCost, childSize] = dfs(neighbor, g);
                    // Update cost with paths between current node and all nodes in child subtree
                    subtreeCost += childCost + childSize; // Paths through this edge
                    subtreeSize += childSize; // Add size of child subtree
                }
            }
            return {subtreeCost, subtreeSize};
        };

        unordered_map<int, long long> groupCosts;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                int currentGroup = group[i];
                auto [cost, _] = dfs(i, currentGroup);
                groupCosts[currentGroup] += cost;
            }
        }

        for (const auto& [g, cost] : groupCosts) {
            totalCost += cost;
        }

        return totalCost;
    }
};
# @lc code=end