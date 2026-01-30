#include <string>
#include <vector>
#include <cstring>

using namespace std;

#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        long long total_count = 0;
        // dp[d][r] stores the number of substrings ending at the previous position 
        // that have a remainder 'r' when divided by 'd'.
        int dp[10][10];
        memset(dp, 0, sizeof(dp));
        
        for (char c : s) {
            int v = c - '0';
            int next_dp[10][10];
            memset(next_dp, 0, sizeof(next_dp));
            
            for (int d = 1; d <= 9; ++d) {
                // Update existing substrings ending at the previous character
                for (int r = 0; r < d; ++r) {
                    if (dp[d][r] > 0) {
                        int next_r = (r * 10 + v) % d;
                        next_dp[d][next_r] += dp[d][r];
                    }
                }
                // Add the new substring consisting only of the current digit
                next_dp[d][v % d]++;
            }
            
            // If the current digit is the divisor (non-zero last digit),
            // add the count of substrings that have remainder 0.
            if (v > 0) {
                total_count += next_dp[v][0];
            }
            
            // Move next_dp state to current dp for the next iteration
            memcpy(dp, next_dp, sizeof(dp));
        }
        
        return total_count;
    }
};
# @lc code=end