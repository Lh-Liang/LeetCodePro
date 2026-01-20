#
# @lc app=leetcode id=3530 lang=cpp
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        // pre[i] stores the bitmask of immediate predecessors of node i
        vector<int> pre(n, 0);
        for (const auto& edge : edges) {
            pre[edge[1]] |= (1 << edge[0]);
        }

        int num_states = 1 << n;
        // dp[mask] = max profit using nodes in mask in a valid topological order
        // Using long long for safety, though int should suffice given constraints
        vector<long long> dp(num_states, -1);
        dp[0] = 0;

        for (int mask = 0; mask < num_states; ++mask) {
            if (dp[mask] == -1) continue;

            // The next node added will be at position k + 1
            int pos = __builtin_popcount(mask) + 1;
            
            // Iterate over all nodes not yet in the mask
            int remaining = (num_states - 1) ^ mask;
            while (remaining > 0) {
                // Get the index of the next available node
                int u = __builtin_ctz(remaining);
                
                // Check if all predecessors of node u are already in the mask
                if ((mask & pre[u]) == pre[u]) {
                    int next_mask = mask | (1 << u);
                    long long next_val = dp[mask] + (long long)score[u] * pos;
                    if (next_val > dp[next_mask]) {
                        dp[next_mask] = next_val;
                    }
                }
                // Clear the least significant set bit
                remaining &= (remaining - 1);
            }
        }

        return (int)dp[num_states - 1];
    }
};
# @lc code=end