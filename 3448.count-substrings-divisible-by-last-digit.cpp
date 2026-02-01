#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#
# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        // dp[d][r] stores the number of substrings ending at the previous position
        // that have remainder r when divided by d.
        long long dp[10][10] = {0};
        long long totalCount = 0;

        for (char c : s) {
            int digit = c - '0';
            long long next_dp[10][10] = {0};

            for (int d = 1; d <= 9; ++d) {
                // For each potential divisor d from 1 to 9, update the remainders 
                // of all substrings ending at the current position.
                // If a substring ending at the previous position had remainder 'r',
                // extending it with 'digit' gives a new remainder: (r * 10 + digit) % d.
                for (int r = 0; r < d; ++r) {
                    if (dp[d][r] > 0) {
                        next_dp[d][(r * 10 + digit) % d] += dp[d][r];
                    }
                }
                // Also account for the new single-digit substring ending at the current position.
                next_dp[d][digit % d]++;
            }

            // Update dp table for the next iteration.
            for (int i = 1; i <= 9; ++i) {
                for (int j = 0; j < i; ++j) {
                    dp[i][j] = next_dp[i][j];
                }
            }

            // If the current digit is non-zero, it acts as the divisor for substrings 
            // ending at this position. Count those that are divisible (remainder 0).
            if (digit > 0) {
                totalCount += dp[digit][0];
            }
        }

        return totalCount;
    }
};
# @lc code=end