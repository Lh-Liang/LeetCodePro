#
# @lc app=leetcode id=3757 lang=cpp
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution {
public:
    int countEffective(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int fullOR = 0;
        for (int num : nums) {
            fullOR |= num;
        }
        
        // Store frequency of each bit in nums
        vector<int> bitFrequency(32, 0);
        for (int num : nums) {
            for (int i = 0; i < 32; ++i) {
                if (num & (1 << i)) {
                    bitFrequency[i]++;
                }
            }
        }

        long long effectiveCount = 0;

        // Calculate effective subsequences by considering contributions of each bit position
        for (int i = 0; i < 32; ++i) {
            if ((fullOR & (1 << i)) && bitFrequency[i] > 0) { // Check if this bit contributes to fullOR
                // Calculate number of ways we can choose subsets from all numbers having this particular bit set
                long long totalSubsets = (1LL << bitFrequency[i]) % MOD;
                // Subtract subsets that do not contribute to reducing the OR, which are when no element with this bit is present 
                long long ineffectiveSubsets = (totalSubsets - 1 + MOD) % MOD; 
                effectiveCount = (effectiveCount + ineffectiveSubsets) % MOD;
            }
        }

        return static_cast<int>(effectiveCount);
    } 
}; 
# @lc code=end