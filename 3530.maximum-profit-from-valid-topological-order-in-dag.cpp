#
# @lc app=leetcode id=3530 lang=cpp
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        vector<int> dep(n, 0);
        // Precompute dependencies as bitmask for each node
        for (auto& e : edges) {
            dep[e[1]] |= (1 << e[0]);
        }
        int N = 1 << n;
        vector<int> dp(N, -1);
        dp[0] = 0;
        for (int mask = 0; mask < N; ++mask) {
            int cnt = __builtin_popcount(mask); // number of nodes placed so far
            for (int i = 0; i < n; ++i) {
                if (!(mask & (1 << i)) && (dep[i] & mask) == dep[i]) {
                    int next_mask = mask | (1 << i);
                    int profit = dp[mask] + score[i] * (cnt + 1);
                    if (dp[next_mask] < profit) {
                        dp[next_mask] = profit;
                    }
                }
            }
        }
        return dp[N - 1];
    }
};
# @lc code=end