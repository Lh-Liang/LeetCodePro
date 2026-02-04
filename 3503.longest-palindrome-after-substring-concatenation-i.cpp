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
        
        // Helper lambda to check if a string is palindrome
        auto isPalindrome = [](const string& str) {
            int left = 0, right = str.size() - 1;
            while (left < right) {
                if (str[left] != str[right]) return false;
                ++left;
                --right;
            }
            return true;
        };
        
        // Check all combinations of prefixes and suffixes for both strings
        for (int i = 0; i <= s.size(); ++i) {
            for (int j = 0; j <= t.size(); ++j) {
                string concat1 = s.substr(0, i) + t.substr(j);
                string concat2 = t.substr(0, j) + s.substr(i);
                if (isPalindrome(concat1)) {
                    maxLength = max(maxLength, static_cast<int>(concat1.size()));
                }
                if (isPalindrome(concat2)) {
                    maxLength = max(maxLength, static_cast<int>(concat2.size()));
                }
            }
        }
        return maxLength;
    }									
};								
# @lc code=end