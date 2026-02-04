#
# @lc app=leetcode id=3559 lang=cpp
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution {
public:
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // Step 1: Construct adjacency list
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        // Helper function for DFS to find path lengths with visited check
        function<int(int, int, int)> dfs = [&](int node, int parent, int target) -> int {
            if (node == target) return 0;
            for (int neighbor : adj[node]) {
                if (neighbor == parent) continue;
                int result = dfs(neighbor, node, target);
                if (result != -1) return result + 1;
            }
            return -1;
        };
        
        const int MOD = 1000000007;
        vector<int> answer;
        
        // Step 2: Process each query
        for (const auto& query : queries) {
            int u = query[0], v = query[1];
            if (u == v) {
                answer.push_back(0); // No valid path or self-path with no edges
                continue;
            }
            int pathLength = dfs(u, -1, v);
            // Step 3: Calculate number of ways to have odd cost
            if (pathLength == -1 || pathLength == 0) {
                answer.push_back(0);
            } else {
                long long validAssignments = ((pathLength % 2 == 0) ? (1LL << (pathLength - 1)) : (1LL << pathLength)) / 2; // Corrected logic for parity-based calculation.
                answer.push_back(validAssignments % MOD);
            }
        }
        return answer;
    }
};
# @lc code=end