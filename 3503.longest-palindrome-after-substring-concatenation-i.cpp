#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#
# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.size();
        int m = t.size();
        int ans = 0;

        auto check_s = [&](int li, int ri) -> bool {
            while (li < ri) {
                if (s[li++] != s[ri--]) return false;
            }
            return true;
        };

        auto check_t = [&](int li, int ri) -> bool {
            while (li < ri) {
                if (t[li++] != t[ri--]) return false;
            }
            return true;
        };

        // Pure substrings of s
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int len = j - i + 1;
                if (check_s(i, j)) {
                    ans = std::max(ans, len);
                }
            }
        }

        // Pure substrings of t
        for (int i = 0; i < m; ++i) {
            for (int j = i; j < m; ++j) {
                int len = j - i + 1;
                if (check_t(i, j)) {
                    ans = std::max(ans, len);
                }
            }
        }

        // Combinations: s[i..j] + t[p..q]
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int la = j - i + 1;
                for (int p = 0; p < m; ++p) {
                    for (int q = p; q < m; ++q) {
                        int lb = q - p + 1;
                        int L = la + lb;
                        if (L <= ans) continue;
                        bool ok = true;
                        for (int k = 0; k < L / 2; ++k) {
                            char cleft = (k < la ? s[i + k] : t[p + k - la]);
                            int rk = L - 1 - k;
                            char cright = (rk < la ? s[i + rk] : t[p + rk - la]);
                            if (cleft != cright) {
                                ok = false;
                                break;
                            }
                        }
                        if (ok) {
                            ans = std::max(ans, L);
                        }
                    }
                }
            }
        }

        return ans;
    }
};
# @lc code=end