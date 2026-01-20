#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution {
    int dp[161][161][2];

    void dfs(int u, int budget, const vector<vector<int>>& adj, const vector<int>& present, const vector<int>& future) {
        // S0[w] stores max profit from children's subtrees if u does NOT buy (children get full price)
        // S1[w] stores max profit from children's subtrees if u DOES buy (children get discount)
        vector<int> S0(budget + 1, 0);
        vector<int> S1(budget + 1, 0);

        for (int v : adj[u]) {
            dfs(v, budget, adj, present, future);
            
            // Update S0 by knapsacking dp[v][...][0]
            for (int b = budget; b >= 0; --b) {
                int best_s0 = 0;
                for (int k = 0; k <= b; ++k) {
                    best_s0 = max(best_s0, S0[b - k] + dp[v][k][0]);
                }
                S0[b] = best_s0;
            }

            // Update S1 by knapsacking dp[v][...][1]
            for (int b = budget; b >= 0; --b) {
                int best_s1 = 0;
                for (int k = 0; k <= b; ++k) {
                    best_s1 = max(best_s1, S1[b - k] + dp[v][k][1]);
                }
                S1[b] = best_s1;
            }
        }

        for (int w = 0; w <= budget; ++w) {
            // dp[u][w][0]: u is offered full price
            // Option 1: u doesn't buy
            dp[u][w][0] = S0[w];
            // Option 2: u buys at full price
            int cost0 = present[u - 1];
            if (w >= cost0) {
                dp[u][w][0] = max(dp[u][w][0], (future[u - 1] - cost0) + S1[w - cost0]);
            }

            // dp[u][w][1]: u is offered discounted price
            // Option 1: u doesn't buy (children still get full price because u didn't buy)
            dp[u][w][1] = S0[w];
            // Option 2: u buys at discount price
            int cost1 = present[u - 1] / 2;
            if (w >= cost1) {
                dp[u][w][1] = max(dp[u][w][1], (future[u - 1] - cost1) + S1[w - cost1]);
            }
        }
    }

public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : hierarchy) {
            adj[edge[0]].push_back(edge[1]);
        }

        // Reset DP table
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= budget; ++j) {
                dp[i][j][0] = dp[i][j][1] = 0;
            }
        }

        dfs(1, budget, adj, present, future);

        // The answer is the max profit for the CEO (node 1) given they are offered full price
        int result = 0;
        for (int w = 0; w <= budget; ++w) {
            result = max(result, dp[1][w][0]);
        }
        return result;
    }
};
# @lc code=end