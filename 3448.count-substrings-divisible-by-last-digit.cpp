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
        long long ans = 0;
        // For each position, consider all substrings ending at i up to length 20
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') continue; // last digit zero is not allowed
            int d = s[i] - '0';
            long long num = 0;
            long long p10 = 1;
            // Go backwards up to 20 characters to avoid overflow
            for (int j = i; j >= 0 && i-j < 20; --j) {
                num = (s[j] - '0') * p10 + num;
                if (num % d == 0) ++ans;
                p10 *= 10;
            }
        }
        return ans;
    }
};
# @lc code=end