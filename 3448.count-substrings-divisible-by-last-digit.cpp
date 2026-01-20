#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    long long countSubstrings(std::string s) {
        long long total = 0;
        // cnt[d][rem] stores the number of substrings ending at the previous index 
        // that have a remainder 'rem' when divided by 'd'.
        long long cnt[10][10] = {0};

        for (char c : s) {
            int digit = c - '0';
            long long next_cnt[10][10] = {0};

            // For every possible non-zero last digit divisor d (1-9)
            for (int d = 1; d <= 9; ++d) {
                // Update existing substring remainders by appending the current digit
                for (int rem = 0; rem < d; ++rem) {
                    if (cnt[d][rem] > 0) {
                        int next_rem = (rem * 10 + digit) % d;
                        next_cnt[d][next_rem] += cnt[d][rem];
                    }
                }
                // Add the current digit itself as a new substring starting at this index
                next_cnt[d][digit % d]++;
            }

            // If the current digit is non-zero, it acts as a divisor for substrings ending here
            if (digit > 0) {
                total += next_cnt[digit][0];
            }

            // Move next_cnt to cnt for the next iteration
            for (int d = 1; d <= 9; ++d) {
                for (int rem = 0; rem < d; ++rem) {
                    cnt[d][rem] = next_cnt[d][rem];
                }
            }
        }

        return total;
    }
};
# @lc code=end