#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int maxLength = 0;
        auto isPalindrome = [](const string& str) {
            return str == string(str.rbegin(), str.rend());
        };
        
        for (int i = 0; i <= s.size(); ++i) {
            for (int j = 0; j <= t.size(); ++j) {
                string combined = s.substr(0, i) + t.substr(0, j);
                if (isPalindrome(combined)) {
                    maxLength = max(maxLength, static_cast<int>(combined.size()));
                }
            }
        }
        return maxLength;
    }
};
# @lc code=end