#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int ans = 0;
        auto is_palindrome = [](const string& x) {
            int l = 0, r = x.size() - 1;
            while (l < r) {
                if (x[l] != x[r]) return false;
                ++l; --r;
            }
            return true;
        };
        int n = s.size(), m = t.size();
        // Check all substrings of s and t concatenated
        for (int i = 0; i <= n; ++i) {
            for (int j = i; j <= n; ++j) {
                string subs = s.substr(i, j - i);
                for (int p = 0; p <= m; ++p) {
                    for (int q = p; q <= m; ++q) {
                        string subt = t.substr(p, q - p);
                        string candidate = subs + subt;
                        if (!candidate.empty() && is_palindrome(candidate)) {
                            int len = candidate.size();
                            if (len > ans) ans = len;
                        }
                    }
                }
            }
        }
        // Check all substrings of s
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                string subs = s.substr(i, j - i);
                if (is_palindrome(subs)) {
                    int len = subs.size();
                    if (len > ans) ans = len;
                }
            }
        }
        // Check all substrings of t
        for (int i = 0; i < m; ++i) {
            for (int j = i + 1; j <= m; ++j) {
                string subt = t.substr(i, j - i);
                if (is_palindrome(subt)) {
                    int len = subt.size();
                    if (len > ans) ans = len;
                }
            }
        }
        return ans;
    }
};
# @lc code=end