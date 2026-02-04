#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#
# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.size(), m = t.size();
        int max_len = 0;
        // Helper: check if a string is palindrome
        auto is_palindrome = [](const string &str) {
            int l = 0, r = str.size() - 1;
            while (l < r) {
                if (str[l] != str[r]) return false;
                ++l; --r;
            }
            return true;
        };
        // Consider all possible substrings of s
        for (int i = 0; i <= n; ++i) {
            for (int j = i; j <= n; ++j) {
                string sub_s = s.substr(i, j - i);
                // Consider all possible substrings of t
                for (int k = 0; k <= m; ++k) {
                    for (int l = k; l <= m; ++l) {
                        string sub_t = t.substr(k, l - k);
                        // Exclude the case where both substrings are empty
                        if (sub_s.empty() && sub_t.empty()) continue;
                        string candidate = sub_s + sub_t;
                        if (is_palindrome(candidate)) {
                            int len = candidate.size();
                            if (len > max_len) max_len = len;
                        }
                    }
                }
            }
        }
        return max_len;
    }
};
# @lc code=end