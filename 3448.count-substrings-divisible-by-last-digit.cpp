#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        int n = s.size();
        long long count = 0;
        // Iterate over each position in the string
        for (int i = 0; i < n; ++i) {
            int last_digit = s[i] - '0';
            if (last_digit == 0) continue; // Skip if last digit is zero
            int current_number = 0;
            // Consider substrings ending at i
            for (int j = i; j >= 0; --j) {
                current_number = (current_number * 10 + (s[j] - '0')) % last_digit;
                if (current_number == 0) {
                    ++count;
                }
            }
        }
        return count;
    }
};
# @lc code=end