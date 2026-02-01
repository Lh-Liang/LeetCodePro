#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    struct Result {
        long long take_parent;
        long long skip_parent;
    };

    Result dfs(int u, int p, const vector<vector<pair<int, int>>>& adj, int k) {
        long long base_sum = 0;
        vector<long long> gains;

        for (const auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v == p) continue;

            Result res_v = dfs(v, u, adj, k);
            
            // Default: don't keep edge (u, v)
            base_sum += res_v.skip_parent;
            
            // Potential gain if we keep edge (u, v)
            long long gain = (long long)w + res_v.take_parent - res_v.skip_parent;
            if (gain > 0) {
                gains.push_back(gain);
            }
        }

        sort(gains.begin(), gains.end(), greater<long long>());

        long long total_gain = 0;
        long long res_take = 0;
        long long res_skip = 0;

        // To calculate skip_parent (can take up to k children)
        // To calculate take_parent (can take up to k-1 children)
        for (int i = 0; i < (int)gains.size(); ++i) {
            if (i < k - 1) {
                total_gain += gains[i];
            } else if (i == k - 1) {
                res_take = base_sum + total_gain;
                total_gain += gains[i];
            }
        }

        if (gains.size() < k) {
            res_take = base_sum + total_gain;
        }
        res_skip = base_sum + total_gain;

        return {res_take, res_skip};
    }

public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }

        return dfs(0, -1, adj, k).skip_parent;
    }
};
# @lc code=end