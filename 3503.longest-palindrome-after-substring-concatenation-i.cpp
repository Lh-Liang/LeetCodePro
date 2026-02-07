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
        auto isPalindrome = [](const string &str) {
            int left = 0, right = str.size() - 1;
            while (left < right) {
                if (str[left++] != str[right--]) return false;
            }
            return true;
        };
        for (int i = 0; i <= s.size(); ++i) {
            for (int j = 0; j <= t.size(); ++j) {
                string combined = s.substr(0, i) + t.substr(j);
                if (isPalindrome(combined)) {
                    maxLength = max(maxLength, int(combined.size()));
                }
            }
        }
        return maxLength;
    }
};
# @lc code=end