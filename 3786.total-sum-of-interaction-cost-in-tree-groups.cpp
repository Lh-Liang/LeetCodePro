#
# @lc app=leetcode id=3786 lang=cpp
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        // Step 1: Build adjacency list
        vector<vector<int>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        // Step 2: Group nodes by group label
        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; ++i) {
            groups[group[i]].push_back(i);
        }
        long long total = 0;
        // Step 3: For each group, calculate pairwise interaction costs
        for (const auto& [g, nodes] : groups) {
            if (nodes.size() < 2) continue;
            vector<bool> in_group(n, false);
            for (int u : nodes) in_group[u] = true;
            // DFS to count group nodes in subtree and compute edge contributions
            function<int(int, int, long long&)> dfs = [&](int u, int parent, long long& cost) -> int {
                int cnt = in_group[u] ? 1 : 0;
                for (int v : adj[u]) {
                    if (v == parent) continue;
                    int sub = dfs(v, u, cost);
                    // Each edge (u-v) contributes sub * (tot - sub)
                    cost += (long long)sub * (nodes.size() - sub);
                    cnt += sub;
                }
                return cnt;
            };
            long long group_cost = 0;
            dfs(nodes[0], -1, group_cost);
            // Each pair is counted twice, so divide by 2
            total += group_cost / 2;
        }
        return total;
    }
};
# @lc code=end