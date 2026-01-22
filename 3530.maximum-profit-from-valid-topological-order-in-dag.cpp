#
# @lc app=leetcode id=3530 lang=cpp
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        // prereq[i] = bitmask of nodes that must come before node i
        vector<int> prereq(n, 0);
        for (auto& e : edges) {
            // edge u -> v means u must come before v
            prereq[e[1]] |= (1 << e[0]);
        }
        
        // dp[mask] = maximum profit when nodes in mask have been processed
        vector<int> dp(1 << n, -1);
        dp[0] = 0;
        
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == -1) continue;
            
            // Position for the next node to add (1-based)
            int pos = __builtin_popcount(mask) + 1;
            
            for (int i = 0; i < n; i++) {
                // Skip if node i is already processed
                if ((mask >> i) & 1) continue;
                // Skip if prerequisites of node i are not all in mask
                if ((prereq[i] & mask) != prereq[i]) continue;
                
                int newMask = mask | (1 << i);
                int newProfit = dp[mask] + score[i] * pos;
                dp[newMask] = max(dp[newMask], newProfit);
            }
        }
        
        return dp[(1 << n) - 1];
    }
};
# @lc code=end