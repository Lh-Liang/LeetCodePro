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
        for (int i = 0; i < n; ++i) {
            int num = 0;
            for (int j = i; j < n; ++j) {
                num = num * 10 + (s[j] - '0');
                int last_digit = s[j] - '0';
                if (last_digit != 0 && num % last_digit == 0) {
                    count++;
                }
            }
        }
        return count;
    }
};
# @lc code=end