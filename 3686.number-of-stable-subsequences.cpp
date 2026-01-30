#include <vector>
using namespace std;

#
# @lc app=leetcode id=3686 lang=cpp
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution {
public:
    int countStableSubsequences(vector<int>& nums) {
        long long mod = 1e9 + 7;
        // dp[parity][count-1]
        // dp[0][0]: ends in one even, dp[0][1]: ends in two evens
        // dp[1][0]: ends in one odd,  dp[1][1]: ends in two odds
        long long dp00 = 0, dp01 = 0, dp10 = 0, dp11 = 0;

        for (int num : nums) {
            int p = num % 2;
            if (p == 0) {
                // New count for subsequences ending in two evens
                long long next_dp01 = (dp01 + dp00) % mod;
                // New count for subsequences ending in one even
                // (starts new, or follows any odd-ending sequence)
                long long next_dp00 = (dp00 + 1 + dp10 + dp11) % mod;
                
                dp01 = next_dp01;
                dp00 = next_dp00;
            } else {
                // New count for subsequences ending in two odds
                long long next_dp11 = (dp11 + dp10) % mod;
                // New count for subsequences ending in one odd
                // (starts new, or follows any even-ending sequence)
                long long next_dp10 = (dp10 + 1 + dp00 + dp01) % mod;

                dp11 = next_dp11;
                dp10 = next_dp10;
            }
        }

        return (dp00 + dp01 + dp10 + dp11) % mod;
    }
};
# @lc code=end