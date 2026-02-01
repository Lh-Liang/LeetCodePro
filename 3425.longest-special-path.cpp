#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    struct Edge {
        int to;
        int weight;
    };
    vector<vector<Edge>> adj;
    vector<int> path_dists;
    int last_pos[50001];
    int max_len;
    int min_nodes;
    const vector<int>* nodes_vals;

    void dfs(int u, int p, int current_dist, int current_depth, int max_ancestor_idx) {
        int val = (*nodes_vals)[u];
        int prev_idx = last_pos[val];
        // The special path ending at u must start at or after start_idx to maintain uniqueness.
        // start_idx is the depth index in the current path.
        int start_idx = max(max_ancestor_idx, prev_idx + 1);
        
        path_dists.push_back(current_dist);
        
        // Path properties from the highest valid ancestor start_idx to u.
        int path_len = current_dist - path_dists[start_idx];
        int num_nodes = current_depth - start_idx + 1;
        
        if (path_len > max_len) {
            max_len = path_len;
            min_nodes = num_nodes;
        } else if (path_len == max_len) {
            if (num_nodes < min_nodes) {
                min_nodes = num_nodes;
            }
        }
        
        int old_pos = last_pos[val];
        last_pos[val] = current_depth;
        
        for (const auto& edge : adj[u]) {
            if (edge.to != p) {
                dfs(edge.to, u, current_dist + edge.weight, current_depth + 1, start_idx);
            }
        }
        
        // Backtrack to maintain the state for other branches in DFS.
        last_pos[val] = old_pos;
        path_dists.pop_back();
    }

public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        adj.assign(n, vector<Edge>());
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }
        
        nodes_vals = &nums;
        // Initialize last_pos with -1 as values are not yet seen in the path.
        for (int i = 0; i <= 50000; ++i) last_pos[i] = -1;
        
        max_len = -1; // Initialize to ensure the first node updates it.
        min_nodes = n + 1;
        
        path_dists.clear();
        path_dists.reserve(n);
        
        // Start DFS from the root node (0).
        dfs(0, -1, 0, 0, 0);
        
        return {max_len, min_nodes};
    }
};
# @lc code=end