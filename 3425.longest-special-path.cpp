#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    int max_len;
    int min_nodes;
    int last_pos[50001];
    vector<int> path_dist;

    void dfs(int u, int p, int d, int current_top, const vector<vector<pair<int, int>>>& adj, const vector<int>& nums) {
        int val = nums[u];
        int prev_idx = last_pos[val];
        
        // Update the window's top index to maintain the unique values invariant.
        int my_top = max(current_top, prev_idx + 1);
        
        // Calculate length and number of nodes for the special path ending at u.
        int current_path_len = d - path_dist[my_top];
        int current_path_nodes = (int)path_dist.size() - my_top;
        
        // Update global maximum length and minimum nodes.
        if (current_path_len > max_len) {
            max_len = current_path_len;
            min_nodes = current_path_nodes;
        } else if (current_path_len == max_len) {
            if (current_path_nodes < min_nodes) {
                min_nodes = current_path_nodes;
            }
        }
        
        // Record current node's depth and recurse.
        int current_depth = (int)path_dist.size() - 1;
        last_pos[val] = current_depth;
        
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v == p) continue;
            
            path_dist.push_back(d + w);
            dfs(v, u, d + w, my_top, adj, nums);
            path_dist.pop_back();
        }
        
        // Backtrack: restore the previous position of this value.
        last_pos[val] = prev_idx;
    }

public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        
        memset(last_pos, -1, sizeof(last_pos));
        path_dist.clear();
        path_dist.push_back(0); // Cumulative distance at the root is 0.
        
        max_len = 0;
        min_nodes = 1;
        
        dfs(0, -1, 0, 0, adj, nums);
        
        return {max_len, min_nodes};
    }
};
# @lc code=end