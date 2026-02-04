#
# @lc app=leetcode id=3504 lang=cpp
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.size(), m = t.size();
        int maxLen = 0;
        string concat = s + t;
        int total = n + m;
        // Helper lambda to expand around center
        auto expand = [&](int l, int r) {
            bool hasS = false, hasT = false;
            while (l >= 0 && r < total && concat[l] == concat[r]) {
                if (l < n) hasS = true;
                if (r >= n) hasT = true;
                // Only consider palindromes that include at least one char from both s and t
                if (hasS && hasT)
                    maxLen = max(maxLen, r - l + 1);
                --l; ++r;
            }
        };
        // Expand around all centers in concatenation
        for (int center = 0; center < total; ++center) {
            expand(center, center);      // Odd length
            expand(center, center + 1);  // Even length
        }
        // Also check palindromes entirely in s or t
        auto maxSingle = [](const string& str) {
            int res = 1, n = str.size();
            for (int i = 0; i < n; ++i) {
                // Odd length
                int l = i, r = i;
                while (l >= 0 && r < n && str[l] == str[r]) {
                    res = max(res, r - l + 1);
                    --l; ++r;
                }
                // Even length
                l = i; r = i + 1;
                while (l >= 0 && r < n && str[l] == str[r]) {
                    res = max(res, r - l + 1);
                    --l; ++r;
                }
            }
            return res;
        };
        maxLen = max(maxLen, maxSingle(s));
        maxLen = max(maxLen, maxSingle(t));
        return maxLen;
    }
};
# @lc code=end