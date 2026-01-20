#
# @lc app=leetcode id=3544 lang=cpp
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    // dp[u][dist][sign]
    // u: node index
    // dist: distance to the nearest inverted ancestor (capped at K)
    // sign: 0 for positive incoming context (even inversions above), 1 for negative (odd inversions above)
    long long dp[50005][55][2];
    int K;
    vector<int> val;

    void dfs(int u, int p) {
        // Initialize dp[u] with the base contribution of u itself
        // If context is 0 (+), u contributes val[u]
        // If context is 1 (-), u contributes -val[u]
        for(int i = 0; i <= K; ++i) {
            dp[u][i][0] = val[u];
            dp[u][i][1] = -val[u];
        }
        
        // Accumulators for the case where we choose to invert u (only valid for i == K)
        // If we invert u, the distance to nearest inverted ancestor for children becomes 1.
        long long sum_inv_children_context_0 = 0; // Sum of children with dist 1, context 0 (+)
        long long sum_inv_children_context_1 = 0; // Sum of children with dist 1, context 1 (-)

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs(v, u);
            
            // Propagate results for the "Don't Invert u" scenarios
            for (int i = 0; i <= K; ++i) {
                int next_dist = (i == K) ? K : i + 1;
                // If i < K, distance increases. If i == K, it stays at "sufficiently far" state K.
                
                // Standard accumulation
                dp[u][i][0] += dp[v][next_dist][0];
                dp[u][i][1] += dp[v][next_dist][1];
            }
            
            // Accumulate for the "Invert u" scenario
            // If u is inverted, v is at distance 1 from the inverted node u.
            // We need to access dp[v][1]...
            int dist_after_inv = 1;
            // In the edge case where K could be less than 1 (though constraint says K>=1), clamp it.
            // If K=1, dist 1 is the max state.
            if (dist_after_inv > K) dist_after_inv = K;
            
            sum_inv_children_context_0 += dp[v][dist_after_inv][0];
            sum_inv_children_context_1 += dp[v][dist_after_inv][1];
        }

        // Apply the choice to Invert u, only valid if i == K
        // 1. Context 0 (+): 
        //    If we invert, u's sign becomes - (relative to global). 
        //    u contributes -val[u].
        //    Children receive context 1 (-).
        long long invert_val_curr_0 = -val[u] + sum_inv_children_context_1;
        dp[u][K][0] = max(dp[u][K][0], invert_val_curr_0);

        // 2. Context 1 (-): 
        //    If we invert, u's sign becomes + (relative to global). 
        //    u contributes val[u].
        //    Children receive context 0 (+).
        long long invert_val_curr_1 = val[u] + sum_inv_children_context_0;
        dp[u][K][1] = max(dp[u][K][1], invert_val_curr_1);
    }

public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        adj.assign(n, vector<int>());
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        val = nums;
        K = k;
        
        dfs(0, -1);
        
        // The root is theoretically at infinite distance from any inverted ancestor (dist K).
        // The initial context is positive (0).
        return dp[0][K][0];
    }
};
# @lc code=end