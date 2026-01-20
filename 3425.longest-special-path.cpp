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
    int max_len;
    int min_nodes;
    int last_seen_depth[50005];
    vector<int> current_path_dist;
    vector<vector<pair<int, int>>> adj;

public:
    void dfs(int u, int p, int current_dist, int current_max_top, const vector<int>& nums) {
        int val = nums[u];
        int prev_depth = last_seen_depth[val];
        
        // The special path ending at u must start at or after the most recent 
        // occurrence of any value already present in the path from the root.
        int my_max_top = max(current_max_top, prev_depth + 1);
        
        current_path_dist.push_back(current_dist);
        int current_depth = (int)current_path_dist.size() - 1;
        
        // The longest special path ending at u starts at depth my_max_top.
        int path_len = current_dist - current_path_dist[my_max_top];
        int num_nodes = current_depth - my_max_top + 1;
        
        if (path_len > max_len) {
            max_len = path_len;
            min_nodes = num_nodes;
        } else if (path_len == max_len) {
            if (num_nodes < min_nodes) {
                min_nodes = num_nodes;
            }
        }
        
        int original_last_depth = last_seen_depth[val];
        last_seen_depth[val] = current_depth;
        
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v != p) {
                dfs(v, u, current_dist + w, my_max_top, nums);
            }
        }
        
        // Backtrack: restore the state for other branches of the DFS
        last_seen_depth[val] = original_last_depth;
        current_path_dist.pop_back();
    }

    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        adj.assign(n, vector<pair<int, int>>());
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }
        
        // Initialize last_seen_depth with -1 to indicate the value hasn't been seen.
        for (int i = 0; i <= 50000; ++i) last_seen_depth[i] = -1;
        
        max_len = 0;
        min_nodes = 1;
        current_path_dist.clear();
        
        dfs(0, -1, 0, 0, nums);
        
        return {max_len, min_nodes};
    }
};
# @lc code=end