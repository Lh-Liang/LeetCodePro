#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3504 lang=cpp
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.length();
        int m = t.length();

        auto get_pals = [&](const string& str) {
            int len = str.length();
            vector<vector<bool>> dp(len, vector<bool>(len, false));
            for (int i = len - 1; i >= 0; --i) {
                for (int j = i; j < len; ++j) {
                    if (str[i] == str[j]) {
                        dp[i][j] = (j - i < 2) ? true : dp[i + 1][j - 1];
                    }
                }
            }
            return dp;
        };

        vector<vector<bool>> pal_s = get_pals(s);
        vector<vector<bool>> pal_t = get_pals(t);

        vector<int> max_p_start_s(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                if (pal_s[i][j]) max_p_start_s[i] = max(max_p_start_s[i], j - i + 1);
            }
        }

        vector<int> max_p_end_t(m + 1, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = i; j < m; ++j) {
                if (pal_t[i][j]) max_p_end_t[j] = max(max_p_end_t[j], j - i + 1);
            }
        }

        string s_rev = s; reverse(s_rev.begin(), s_rev.end());
        string t_rev = t; reverse(t_rev.begin(), t_rev.end());

        auto get_max_match = [&](const string& target, const string& source_rev) {
            int n1 = target.length(), n2 = source_rev.length();
            vector<int> res(n1, 0);
            for (int i = 0; i < n2; ++i) {
                int curr_match = 0;
                for (int j = 0; j < n1 && i + j < n2; ++j) {
                    if (target[j] == source_rev[i + j]) {
                        curr_match++;
                        res[j] = max(res[j], curr_match);
                    } else {
                        break;
                    }
                }
            }
            return res;
        };

        vector<int> max_x_end_s(n, 0);
        for (int i = 0; i < m; ++i) {
            int match = 0;
            for (int j = 0; j < n && i + j < m; ++j) {
                if (t_rev[i + j] == s[j]) match = 0; 
            }
        }
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int k = 0;
                while (i - k >= 0 && j + k < m && s[i - k] == t_rev[j + k]) {
                    k++;
                    max_x_end_s[i] = max(max_x_end_s[i], k);
                }
            }
        }

        vector<int> max_xrev_start_t(m, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int k = 0;
                while (i + k < m && j + k < n && t[i + k] == s_rev[j + k]) {
                    k++;
                    max_xrev_start_t[i] = max(max_xrev_start_t[i], k);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int p_len = (i + 1 < n) ? max_p_start_s[i + 1] : 0;
            ans = max(ans, 2 * max_x_end_s[i] + p_len);
        }
        for (int i = 0; i < m; ++i) {
            int p_len = (i > 0) ? max_p_end_t[i - 1] : 0;
            ans = max(ans, 2 * max_xrev_start_t[i] + p_len);
        }

        for (int i = 0; i < n; ++i) ans = max(ans, max_p_start_s[i]);
        for (int i = 0; i < m; ++i) ans = max(ans, max_p_end_t[i]);

        return ans;
    }
};
# @lc code=end