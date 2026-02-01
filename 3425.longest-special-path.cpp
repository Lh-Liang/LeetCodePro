#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int max_len = -1;
    int min_nodes = 1e9;
    vector<vector<pair<int, int>>> adj;
    int last_seen_depth[50001];
    int path_dists[50005];

    void dfs(int u, int p, int depth, int current_dist, int current_start_depth, const vector<int>& nums) {
        int val = nums[u];
        int prev_depth = last_seen_depth[val];
        
        // The path must start after the last occurrence of the current node's value
        int start_depth = max(current_start_depth, prev_depth + 1);
        path_dists[depth + 1] = current_dist;
        
        int length = current_dist - path_dists[start_depth];
        int nodes = depth - start_depth + 1;
        
        if (length > max_len) {
            max_len = length;
            min_nodes = nodes;
        } else if (length == max_len) {
            min_nodes = min(min_nodes, nodes);
        }
        
        last_seen_depth[val] = depth;
        
        for (auto& edge : adj[u]) {
            if (edge.first != p) {
                dfs(edge.first, u, depth + 1, current_dist + edge.second, start_depth, nums);
            }
        }
        
        // Backtrack
        last_seen_depth[val] = prev_depth;
    }

public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        adj.assign(n, vector<pair<int, int>>());
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        
        for (int i = 0; i < 50001; ++i) last_seen_depth[i] = -1;
        path_dists[0] = 0;
        max_len = 0;
        min_nodes = 1;
        
        dfs(0, -1, 0, 0, 0, nums);
        
        return {max_len, min_nodes};
    }
};