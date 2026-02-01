#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    long long countSubstrings(string s) {
        long long ans = 0;
        // dp[d][r] stores the number of substrings ending at the current position
        // that have a remainder r when divided by d.
        long long dp[10][10];
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                dp[i][j] = 0;
            }
        }
        
        for (char c : s) {
            int v = c - '0';
            long long next_dp[10][10];
            for (int i = 0; i < 10; ++i) {
                for (int j = 0; j < 10; ++j) {
                    next_dp[i][j] = 0;
                }
            }
            
            for (int d = 1; d <= 9; ++d) {
                // Update existing substrings ending at previous index
                for (int r = 0; r < d; ++r) {
                    if (dp[d][r] > 0) {
                        next_dp[d][(r * 10 + v) % d] += dp[d][r];
                    }
                }
                // Add the new substring starting and ending at the current digit
                next_dp[d][v % d]++;
            }
            
            // Copy next_dp to dp
            for (int d = 1; d <= 9; ++d) {
                for (int r = 0; r < d; ++r) {
                    dp[d][r] = next_dp[d][r];
                }
            }
            
            // If the current digit is non-zero, it is the divisor
            if (v > 0) {
                ans += dp[v][0];
            }
        }
        
        return ans;
    }
};
# @lc code=end