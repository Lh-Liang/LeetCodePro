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
        string total = s + t;
        int N = n + m;
        int res = 0;
        // Check palindromes centered at every possible center (odd/even)
        for(int center = 0; center < N; ++center) {
            // Odd length palindrome
            int l = center, r = center;
            while(l >= 0 && r < N && total[l] == total[r]) {
                // At least one char from s and one from t
                if (l < n && r >= n) {
                    res = max(res, r - l + 1);
                }
                l--; r++;
            }
            // Even length palindrome
            l = center; r = center + 1;
            while(l >= 0 && r < N && total[l] == total[r]) {
                if (l < n && r >= n) {
                    res = max(res, r - l + 1);
                }
                l--; r++;
            }
        }
        // Also, palindromes fully in s and fully in t
        auto getLongest = [](const string& str) {
            int len = str.size(), best = 0;
            for (int i = 0; i < len; ++i) {
                int l = i, r = i;
                while (l >= 0 && r < len && str[l] == str[r]) {
                    best = max(best, r - l + 1);
                    l--; r++;
                }
                l = i; r = i+1;
                while (l >= 0 && r < len && str[l] == str[r]) {
                    best = max(best, r - l + 1);
                    l--; r++;
                }
            }
            return best;
        };
        res = max(res, getLongest(s));
        res = max(res, getLongest(t));
        return res;
    }
};
# @lc code=end