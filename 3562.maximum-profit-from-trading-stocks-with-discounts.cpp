#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        // Adjacency list for the tree
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : hierarchy) {
            adj[edge[0]].push_back(edge[1]);
        }

        // DFS function
        // Returns a pair of vectors: {dp_parent_no_buy, dp_parent_buy}
        // Each vector is of size budget + 1, where vec[c] = max profit with cost c
        // If a cost is unreachable, we can use a very small number, but since we start with 0 cost 0 profit, 
        // and only add, we can just initialize with -1e9 or similar to denote invalid, 
        // or just handle valid states explicitly. 
        // Here, initializing with a specific value for 'impossible' is safer.
        
        const int INF = 1e9;
        
        // Helper to merge knapsacks
        auto merge = [&](const vector<int>& current_dp, const vector<int>& child_dp) {
            vector<int> next_dp(budget + 1, -INF);
            for (int b = 0; b <= budget; ++b) {
                if (current_dp[b] == -INF) continue;
                for (int cb = 0; cb <= budget - b; ++cb) {
                    if (child_dp[cb] == -INF) continue;
                    next_dp[b + cb] = max(next_dp[b + cb], current_dp[b] + child_dp[cb]);
                }
            }
            return next_dp;
        };

        function<pair<vector<int>, vector<int>>(int)> dfs = [&](int u) {
            // 1. Calculate aggregated results from children
            // agg_no_buy: max profit from subtree children assuming u DOES NOT buy
            // agg_buy: max profit from subtree children assuming u DOES buy
            
            vector<int> agg_no_buy(budget + 1, -INF);
            vector<int> agg_buy(budget + 1, -INF);
            
            // Base case: 0 cost, 0 profit
            agg_no_buy[0] = 0;
            agg_buy[0] = 0;

            for (int v : adj[u]) {
                pair<vector<int>, vector<int>> child_res = dfs(v);
                // If u doesn't buy, v sees parent_bought=false -> child_res.first
                agg_no_buy = merge(agg_no_buy, child_res.first);
                // If u buys, v sees parent_bought=true -> child_res.second
                agg_buy = merge(agg_buy, child_res.second);
            }

            // 2. Construct result for u
            // res.first: parent of u didn't buy
            // res.second: parent of u bought
            
            vector<int> res_parent_no_buy = agg_no_buy; // Initialize with option where u doesn't buy
            vector<int> res_parent_buy = agg_no_buy;    // Initialize with option where u doesn't buy
            
            // Option where u buys:
            // Case A: parent of u didn't buy. u pays full price.
            int cost_full = present[u - 1];
            int profit_full = future[u - 1] - cost_full;
            
            for (int b = 0; b <= budget - cost_full; ++b) {
                if (agg_buy[b] != -INF) {
                    res_parent_no_buy[b + cost_full] = max(res_parent_no_buy[b + cost_full], agg_buy[b] + profit_full);
                }
            }

            // Case B: parent of u bought. u pays half price.
            int cost_half = present[u - 1] / 2;
            int profit_half = future[u - 1] - cost_half;
            
            for (int b = 0; b <= budget - cost_half; ++b) {
                if (agg_buy[b] != -INF) {
                    res_parent_buy[b + cost_half] = max(res_parent_buy[b + cost_half], agg_buy[b] + profit_half);
                }
            }
            
            return make_pair(res_parent_no_buy, res_parent_buy);
        };

        pair<vector<int>, vector<int>> result = dfs(1);
        
        // Since 1 has no parent, we look at result.first (parent didn't buy)
        int max_p = 0;
        for (int p : result.first) {
            max_p = max(max_p, p);
        }
        return max_p;
    }
};
# @lc code=end