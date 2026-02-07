#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        long long count = 0;
        int n = s.size();
        
        // Iterate over each end position of the substring
        for (int j = 0; j < n; ++j) {
            int lastDigit = s[j] - '0';
            if (lastDigit == 0) continue; // Ignore if last digit is zero
            
            int num = 0;
            int multiplier = 1;
            // Consider substrings ending at j and check divisibility by lastDigit
            for (int i = j; i >= 0; --i) {
                num += (s[i] - '0') * multiplier; // Build number from right to left using multiplication to avoid overflow issues
                if (num % lastDigit == 0) count++; // Check divisibility by lastDigit
                multiplier *= 10;
                // If leading parts become zero due to previous zeroes, continue checking further unless it's a single zero.
            }
        }
        return count;
    }
};
# @lc code=end