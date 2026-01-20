#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution {
public:
    bool isPalindrome(const string& str) {
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str[left] != str[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    int longestPalindrome(string s, string t) {
        int n = s.length();
        int m = t.length();
        int maxLen = 0;

        // Iterate over all substrings of s (including empty)
        for (int i = 0; i <= n; ++i) {
            for (int len_s = 0; i + len_s <= n; ++len_s) {
                string sub_s = s.substr(i, len_s);
                
                // Iterate over all substrings of t (including empty)
                for (int j = 0; j <= m; ++j) {
                    for (int len_t = 0; j + len_t <= m; ++len_t) {
                        string sub_t = t.substr(j, len_t);
                        
                        if (sub_s.empty() && sub_t.empty()) continue;

                        string combined = sub_s + sub_t;
                        if (isPalindrome(combined)) {
                            maxLen = max(maxLen, (int)combined.length());
                        }
                    }
                }
            }
        }
        return maxLen;
    }
};
# @lc code=end