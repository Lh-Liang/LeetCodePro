#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
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

    long long max_len = 0;
    int min_nodes = 1;
    int last_pos[50005];
    long long path_dists[50005];

    void dfs(int u, int p, int depth, long long curr_dist, int m1, int m2, const vector<vector<Edge>>& adj, const vector<int>& nums) {
        int val = nums[u];
        int prev_depth = last_pos[val];

        // Update the two largest conflict depths encountered on this path
        int nm1 = m1, nm2 = m2;
        if (prev_depth > nm1) {
            nm2 = nm1;
            nm1 = prev_depth;
        } else if (prev_depth > nm2) {
            nm2 = prev_depth;
        }

        // The special path starts after the second most recent conflict
        long long L = curr_dist - path_dists[nm2];
        int C = depth - nm2;

        if (L > max_len) {
            max_len = L;
            min_nodes = C;
        } else if (L == max_len) {
            min_nodes = min(min_nodes, C);
        }

        path_dists[depth] = curr_dist;
        last_pos[val] = depth;

        for (const auto& edge : adj[u]) {
            if (edge.to != p) {
                dfs(edge.to, u, depth + 1, curr_dist + edge.weight, nm1, nm2, adj, nums);
            }
        }

        // Backtrack: restore the previous depth for this value
        last_pos[val] = prev_depth;
    }

public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<Edge>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        // Initialize: use 1-based depth. depth 0 is a dummy for distance calculation.
        for (int i = 0; i < 50005; ++i) last_pos[i] = 0;
        path_dists[0] = 0;
        max_len = 0;
        min_nodes = 1e9; // Will be updated by the first node (root)

        dfs(0, -1, 1, 0, 0, 0, adj, nums);

        return {(int)max_len, min_nodes};
    }
};
# @lc code=end