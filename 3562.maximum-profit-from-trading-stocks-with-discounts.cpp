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
        for (auto& h : hierarchy) {
            int u = h[0] - 1, v = h[1] - 1;
            tree[u].push_back(v);
        }
        // dp[u][0][c]: max profit for u and subtree with cost c if boss doesn't buy (no discount)
        // dp[u][1][c]: max profit for u and subtree with cost c if boss buys (discounted price for u)
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(2, vector<int>(budget + 1, -1e9)) );

        function<void(int)> dfs = [&](int u) {
            for (int b = 0; b <= budget; ++b) {
                dp[u][0][b] = dp[u][1][b] = 0;
            }
            int cost = present[u];
            int profit = future[u] - present[u];
            if (cost <= budget) dp[u][0][cost] = profit;
            int dcost = present[u] / 2;
            int dprofit = future[u] - dcost;
            if (dcost <= budget) dp[u][1][dcost] = dprofit;
            dp[u][0][0] = dp[u][1][0] = 0;
            for (int v : tree[u]) {
                dfs(v);
                vector<vector<int>> ndp(2, vector<int>(budget + 1, -1e9));
                for (int x = 0; x <= budget; ++x) {
                    for (int y = 0; y <= budget - x; ++y) {
                        ndp[0][x + y] = max(ndp[0][x + y], dp[u][0][x] + max(dp[v][0][y], dp[v][1][y]));
                        ndp[1][x + y] = max(ndp[1][x + y], dp[u][1][x] + dp[v][1][y]);
                    }
                }
                dp[u] = ndp;
            }
        };
        dfs(0);
        int ans = 0;
        for (int b = 0; b <= budget; ++b) {
            ans = max({ans, dp[0][0][b], dp[0][1][b]});
        }
        return ans;
    }
};
# @lc code=end