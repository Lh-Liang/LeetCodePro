#
# @lc app=leetcode id=3509 lang=cpp
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        const int OFFSET = 901;
        const int MAX_SUM = 2 * OFFSET;
        
        // dp[parity][sum] = bitset of achievable products
        // parity 0 = even length (next element contributes +)
        // parity 1 = odd length (next element contributes -)
        vector<vector<bitset<5001>>> dp(2, vector<bitset<5001>>(MAX_SUM));
        
        for (int num : nums) {
            vector<vector<bitset<5001>>> temp(2, vector<bitset<5001>>(MAX_SUM));
            
            // Start a new subsequence with this element
            if (num <= limit && num + OFFSET >= 0 && num + OFFSET < MAX_SUM) {
                temp[1][num + OFFSET][num] = true;
            }
            
            // Extend existing subsequences
            for (int p = 0; p < 2; p++) {
                for (int s = 0; s < MAX_SUM; s++) {
                    if (dp[p][s].none()) continue;
                    
                    int new_s = s + ((p == 0) ? num : -num);
                    int new_p = 1 - p;
                    
                    if (new_s < 0 || new_s >= MAX_SUM) continue;
                    
                    // Iterate through set bits efficiently
                    for (size_t prod = dp[p][s]._Find_first(); prod < dp[p][s].size(); prod = dp[p][s]._Find_next(prod)) {
                        long long new_prod = (long long)prod * num;
                        if (new_prod <= limit) {
                            temp[new_p][new_s][(int)new_prod] = true;
                        }
                    }
                }
            }
            
            // Merge temp into dp
            for (int p = 0; p < 2; p++) {
                for (int s = 0; s < MAX_SUM; s++) {
                    dp[p][s] |= temp[p][s];
                }
            }
        }
        
        int target = k + OFFSET;
        if (target < 0 || target >= MAX_SUM) return -1;
        
        int ans = -1;
        for (int p = 0; p < 2; p++) {
            for (int prod = limit; prod >= 0; prod--) {
                if (dp[p][target][prod]) {
                    ans = max(ans, prod);
                    break;
                }
            }
        }
        
        return ans;
    }
};
# @lc code=end