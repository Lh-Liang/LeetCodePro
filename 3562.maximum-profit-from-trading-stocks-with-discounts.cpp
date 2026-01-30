#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    int N;
    int B;
    vector<int> P, F;
    vector<vector<int>> adj;
    // memo[node][parent_bought] = vector of size B+1
    vector<int> memo[161][2];
    const int INF = 1e9;

    vector<int> solve(int u, int parent_bought) {
        if (!memo[u][parent_bought].empty()) return memo[u][parent_bought];

        // Case 1: Employee u buys their stock
        int cost_buy = parent_bought ? (P[u-1] / 2) : P[u-1];
        int profit_buy = F[u-1] - cost_buy;
        
        vector<int> dp_buy(B + 1, -INF);
        if (cost_buy <= B) {
            dp_buy[cost_buy] = profit_buy;
        }
        
        for (int v : adj[u]) {
            vector<int> sub = solve(v, 1);
            vector<int> next_dp(B + 1, -INF);
            for (int b1 = 0; b1 <= B; ++b1) {
                if (dp_buy[b1] <= -INF) continue;
                for (int b2 = 0; b1 + b2 <= B; ++b2) {
                    if (sub[b2] <= -INF) continue;
                    next_dp[b1 + b2] = max(next_dp[b1 + b2], dp_buy[b1] + sub[b2]);
                }
            }
            dp_buy = next_dp;
        }

        // Case 2: Employee u does not buy their stock
        vector<int> dp_not_buy(B + 1, -INF);
        dp_not_buy[0] = 0;
        
        for (int v : adj[u]) {
            vector<int> sub = solve(v, 0);
            vector<int> next_dp(B + 1, -INF);
            for (int b1 = 0; b1 <= B; ++b1) {
                if (dp_not_buy[b1] <= -INF) continue;
                for (int b2 = 0; b1 + b2 <= B; ++b2) {
                    if (sub[b2] <= -INF) continue;
                    next_dp[b1 + b2] = max(next_dp[b1 + b2], dp_not_buy[b1] + sub[b2]);
                }
            }
            dp_not_buy = next_dp;
        }

        vector<int> res(B + 1, -INF);
        for (int b = 0; b <= B; ++b) {
            res[b] = max(dp_buy[b], dp_not_buy[b]);
        }
        return memo[u][parent_bought] = res;
    }

public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        N = n;
        B = budget;
        P = present;
        F = future;
        adj.assign(n + 1, vector<int>());
        for (auto& edge : hierarchy) {
            adj[edge[0]].push_back(edge[1]);
        }
        
        for (int i = 0; i <= n; ++i) {
            memo[i][0].clear();
            memo[i][1].clear();
        }
        
        vector<int> res = solve(1, 0);
        int max_total_profit = 0;
        for (int b = 0; b <= B; ++b) {
            max_total_profit = max(max_total_profit, res[b]);
        }
        return max_total_profit;
    }
};
# @lc code=end