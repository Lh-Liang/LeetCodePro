#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> tree(n);
        for (const auto& edge : hierarchy) {
            int u = edge[0] - 1, v = edge[1] - 1;
            tree[u].push_back(v);
        }
        // dp[node][discount][cost] = max profit; discount: 0=no discount, 1=discount
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(2, vector<int>(budget+1, -1)));
        function<void(int)> dfs = [&](int u) {
            // Base initialization
            for (int disc = 0; disc <= 1; ++disc) {
                fill(dp[u][disc].begin(), dp[u][disc].end(), 0);
            }
            // First, not buy at u: just combine children
            for (int disc = 0; disc <= 1; ++disc) {
                vector<int> cur(budget+1, 0);
                for (int v : tree[u]) {
                    dfs(v);
                    vector<int> next(budget+1, 0);
                    for (int c1 = 0; c1 <= budget; ++c1) {
                        if (cur[c1] < 0) continue;
                        for (int c2 = 0; c2 + c1 <= budget; ++c2) {
                            if (dp[v][0][c2] < 0) continue;
                            next[c1+c2] = max(next[c1+c2], cur[c1] + dp[v][0][c2]);
                        }
                    }
                    swap(cur, next);
                }
                for (int c = 0; c <= budget; ++c) {
                    dp[u][disc][c] = max(dp[u][disc][c], cur[c]);
                }
            }
            // Then, buy at u (with or without discount)
            for (int disc = 0; disc <= 1; ++disc) {
                int buy_price = disc ? present[u] / 2 : present[u];
                int profit = future[u] - buy_price;
                if (buy_price > budget) continue;
                vector<int> cur(budget+1, -1);
                cur[buy_price] = profit;
                for (int v : tree[u]) {
                    vector<int> next(budget+1, -1);
                    for (int c1 = 0; c1 <= budget; ++c1) {
                        if (cur[c1] < 0) continue;
                        for (int c2 = 0; c2 + c1 <= budget; ++c2) {
                            if (dp[v][1][c2] < 0) continue;
                            next[c1+c2] = max(next[c1+c2], cur[c1] + dp[v][1][c2]);
                        }
                    }
                    swap(cur, next);
                }
                for (int c = 0; c <= budget; ++c) {
                    if (cur[c] >= 0)
                        dp[u][disc][c] = max(dp[u][disc][c], cur[c]);
                }
            }
        };
        dfs(0);
        int ans = 0;
        for (int c = 0; c <= budget; ++c) {
            ans = max(ans, dp[0][0][c]);
        }
        return ans;
    }
};
# @lc code=end