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
        // Precompute predecessors for each node as a bitmask
        // pre[i] contains a bitmask of all nodes that must precede node i
        vector<int> pre(n, 0);
        for (const auto& edge : edges) {
            pre[edge[1]] |= (1 << edge[0]);
        }

        // dp[mask] stores the maximum profit using nodes in mask.
        // Initialize with -1 to represent unreachable states.
        int num_states = 1 << n;
        vector<int> dp(num_states, -1);
        dp[0] = 0;

        for (int mask = 0; mask < num_states; ++mask) {
            if (dp[mask] == -1) continue;

            // The position of the next node to be added is popcount(mask) + 1
            int k = __builtin_popcount(mask) + 1;
            
            // Try adding each node i that is not yet in the mask
            int remaining = (num_states - 1) ^ mask;
            while (remaining) {
                int i = __builtin_ctz(remaining);
                
                // Check if the topological constraint is satisfied:
                // All predecessors of node i must be present in the current mask.
                if ((pre[i] & mask) == pre[i]) {
                    int next_mask = mask | (1 << i);
                    int current_val = dp[mask] + score[i] * k;
                    if (current_val > dp[next_mask]) {
                        dp[next_mask] = current_val;
                    }
                }
                // Remove the lowest set bit to continue iteration
                remaining &= (remaining - 1);
            }
        }

        return dp[num_states - 1];
    }
};
# @lc code=end