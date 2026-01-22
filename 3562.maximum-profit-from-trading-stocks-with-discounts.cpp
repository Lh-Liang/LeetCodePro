//
// @lc app=leetcode id=3562 lang=cpp
//
// [3562] Maximum Profit from Trading Stocks with Discounts
//

// @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> children(n + 1);
        for (auto& h : hierarchy) {
            children[h[0]].push_back(h[1]);
        }
        
        const int NEG_INF = -100000000;
        
        // dfs returns {dp0, dp1} where:
        // dp0[b] = max profit when node doesn't buy, using budget b
        // dp1[b] = max profit when node buys at full price, using budget b
        function<pair<vector<int>, vector<int>>(int)> dfs = [&](int node) -> pair<vector<int>, vector<int>> {
            vector<int> dp0(budget + 1, NEG_INF);
            vector<int> dp1(budget + 1, NEG_INF);
            
            // Initialize with just the current node
            dp0[0] = 0;
            int cost = present[node - 1];
            if (cost <= budget) {
                dp1[cost] = future[node - 1] - cost;
            }
            
            for (int child : children[node]) {
                auto [cdp0, cdp1] = dfs(child);
                
                int discount = present[child - 1] - present[child - 1] / 2;
                
                vector<int> new_dp0(budget + 1, NEG_INF);
                vector<int> new_dp1(budget + 1, NEG_INF);
                
                // Combine dp0 with child's dp (child pays full price)
                for (int b0 = 0; b0 <= budget; b0++) {
                    if (dp0[b0] == NEG_INF) continue;
                    for (int bc = 0; b0 + bc <= budget; bc++) {
                        if (cdp0[bc] > NEG_INF) {
                            new_dp0[b0 + bc] = max(new_dp0[b0 + bc], dp0[b0] + cdp0[bc]);
                        }
                        if (cdp1[bc] > NEG_INF) {
                            new_dp0[b0 + bc] = max(new_dp0[b0 + bc], dp0[b0] + cdp1[bc]);
                        }
                    }
                }
                
                // Combine dp1 with child's dp (child gets discount if buying)
                for (int b1 = 0; b1 <= budget; b1++) {
                    if (dp1[b1] == NEG_INF) continue;
                    for (int bc = 0; bc <= budget; bc++) {
                        // Child doesn't buy
                        if (cdp0[bc] > NEG_INF && b1 + bc <= budget) {
                            new_dp1[b1 + bc] = max(new_dp1[b1 + bc], dp1[b1] + cdp0[bc]);
                        }
                        // Child buys with discount
                        if (cdp1[bc] > NEG_INF) {
                            int new_cost = b1 + bc - discount;
                            if (new_cost >= 0 && new_cost <= budget) {
                                new_dp1[new_cost] = max(new_dp1[new_cost], dp1[b1] + cdp1[bc] + discount);
                            }
                        }
                    }
                }
                
                dp0 = move(new_dp0);
                dp1 = move(new_dp1);
            }
            
            return {dp0, dp1};
        };
        
        auto [dp0, dp1] = dfs(1);
        
        int ans = 0;
        for (int b = 0; b <= budget; b++) {
            ans = max(ans, max(dp0[b], dp1[b]));
        }
        
        return ans;
    }
};
// @lc code=end