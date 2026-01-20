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
            vector<long long> diffs;

            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (v == p) continue;

                auto [res0, res1] = self(self, v, u);
                // res0: max sum if v can connect to u
                // res1: max sum if v cannot connect to u (already has k connections)
                
                base_sum += res1;
                long long diff = (res0 + w) - res1;
                if (diff > 0) {
                    diffs.push_back(diff);
                }
            }

            sort(diffs.rbegin(), diffs.rend());

            long long sum0 = base_sum; // can take k-1 edges to children
            long long sum1 = base_sum; // can take k edges to children

            for (int i = 0; i < diffs.size(); ++i) {
                if (i < k - 1) sum0 += diffs[i];
                if (i < k) sum1 += diffs[i];
            }

            return {sum0, sum1};
        };

        auto result = dfs(dfs, 0, -1);
        return result.second;
    }
};
# @lc code=end