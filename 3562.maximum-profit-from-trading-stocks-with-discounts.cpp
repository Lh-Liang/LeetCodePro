#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> children(n + 1);
        for (auto& h : hierarchy) {
            children[h[0]].push_back(h[1]);
        }
        const int INF = 1e9 + 5;
        vector<vector<vector<int>>> memo(n + 1, vector<vector<int>>(2, vector<int>(budget + 1, -INF)));
        vector<vector<bool>> computed(n + 1, vector<bool>(2, false));

        auto dfs = [&](auto&& self, int u, int disc) -> vector<int> {
            if (computed[u][disc]) {
                return memo[u][disc];
            }
            computed[u][disc] = true;
            vector<int>& res = memo[u][disc];

            int cost_full = present[u - 1];
            int cost_disc = cost_full / 2;
            int my_cost = disc ? cost_disc : cost_full;
            int my_prof = future[u - 1] - my_cost;

            // comb_no: u not buying, children no discount
            vector<int> comb_no(budget + 1, -INF);
            comb_no[0] = 0;
            for (int v : children[u]) {
                vector<int> dpv = self(self, v, 0);
                vector<int> newc(budget + 1, -INF);
                for (int s = 0; s <= budget; ++s) {
                    if (comb_no[s] == -INF) continue;
                    for (int t = 0; t <= budget - s; ++t) {
                        if (dpv[t] != -INF) {
                            newc[s + t] = max(newc[s + t], comb_no[s] + dpv[t]);
                        }
                    }
                }
                comb_no = std::move(newc);
            }

            // comb_yes: u buying, children get discount
            vector<int> comb_yes(budget + 1, -INF);
            comb_yes[0] = 0;
            for (int v : children[u]) {
                vector<int> dpv = self(self, v, 1);
                vector<int> newc(budget + 1, -INF);
                for (int s = 0; s <= budget; ++s) {
                    if (comb_yes[s] == -INF) continue;
                    for (int t = 0; t <= budget - s; ++t) {
                        if (dpv[t] != -INF) {
                            newc[s + t] = max(newc[s + t], comb_yes[s] + dpv[t]);
                        }
                    }
                }
                comb_yes = std::move(newc);
            }

            // Combine
            for (int k = 0; k <= budget; ++k) {
                res[k] = comb_no[k];
                if (k >= my_cost && comb_yes[k - my_cost] != -INF) {
                    res[k] = max(res[k], my_prof + comb_yes[k - my_cost]);
                }
            }
            return res;
        };

        vector<int> root_dp = dfs(dfs, 1, 0);
        int ans = 0;
        for (int k = 0; k <= budget; ++k) {
            if (root_dp[k] > ans) {
                ans = root_dp[k];
            }
        }
        return ans;
    }
};
# @lc code=end