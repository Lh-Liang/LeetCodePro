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
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }

        auto dfs = [&](auto self, int u, int p) -> pair<long long, long long> {
            long long base_sum = 0;
            vector<long long> gains;

            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (v == p) continue;

                auto [dp_v_0, dp_v_1] = self(self, v, u);
                
                // Base: assume we don't take edge (u, v)
                base_sum += dp_v_0;
                
                // Gain if we take edge (u, v)
                long long gain = (long long)w + dp_v_1 - dp_v_0;
                if (gain > 0) {
                    gains.push_back(gain);
                }
            }

            sort(gains.rbegin(), gains.rend());

            long long res0 = base_sum; // u can take up to k children
            long long res1 = base_sum; // u can take up to k-1 children (1 slot for parent)

            for (int i = 0; i < gains.size(); ++i) {
                if (i < k) res0 += gains[i];
                if (i < k - 1) res1 += gains[i];
            }

            return {res0, res1};
        };

        return dfs(dfs, 0, -1).first;
    }
};
# @lc code=end