#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
#include <string>
#include <vector>
#include <array>

using namespace std;

class Solution {
public:
    long long countSubstrings(string s) {
        // dp[divisor][remainder] stores the count of substrings ending at current index
        // having 'remainder' when divided by 'divisor'.
        long long dp[10][10] = {0};
        long long totalCount = 0;

        for (char c : s) {
            int digit = c - '0';
            long long next_dp[10][10] = {0};

            for (int d = 1; d <= 9; ++d) {
                // Transition existing substrings to the new index
                for (int r = 0; r < d; ++r) {
                    if (dp[d][r] > 0) {
                        int next_r = (r * 10 + digit) % d;
                        next_dp[d][next_r] += dp[d][r];
                    }
                }
                // Add the new single-digit substring [i...i]
                next_dp[d][digit % d]++;
            }

            // If the current digit is a valid divisor, add count of substrings with remainder 0
            if (digit > 0) {
                totalCount += next_dp[digit][0];
            }
            
            // Update DP table for the next iteration
            for (int d = 1; d <= 9; ++d) {
                for (int r = 0; r < d; ++r) {
                    dp[d][r] = next_dp[d][r];
                }
            }
        }

        return totalCount;
    }
};
# @lc code=end