#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution {
    struct DP {
        long long f0; // Max sum if node u can use k slots
        long long f1; // Max sum if node u can use k-1 slots
    };

    vector<vector<pair<int, int>>> adj;
    int K;

    DP dfs(int u, int p) {
        long long base_sum = 0;
        vector<long long> positive_gains;

        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v == p) continue;

            DP res = dfs(v, u);
            // By default, we assume we don't keep the edge (u, v)
            base_sum += res.f0;
            
            // Gain if we keep the edge (u, v): (w + dp[v][1]) - dp[v][0]
            long long gain = (long long)w + res.f1 - res.f0;
            if (gain > 0) {
                positive_gains.push_back(gain);
            }
        }

        // Sort gains descending to pick the best edges to keep
        sort(positive_gains.begin(), positive_gains.end(), greater<long long>());

        long long f0 = base_sum;
        for (int i = 0; i < min((int)positive_gains.size(), K); ++i) {
            f0 += positive_gains[i];
        }

        long long f1 = base_sum;
        for (int i = 0; i < min((int)positive_gains.size(), K - 1); ++i) {
            f1 += positive_gains[i];
        }

        return {f0, f1};
    }

public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        adj.assign(n, vector<pair<int, int>>());
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        K = k;
        return dfs(0, -1).f0;
    }
};
# @lc code=end