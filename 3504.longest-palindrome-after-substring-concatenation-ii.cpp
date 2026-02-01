#
# @lc app=leetcode id=3504 lang=cpp
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.length(), m = t.length();

        // Helper to find longest palindrome starting at each index using Manacher-like logic or pre-calculation
        auto get_longest_starting = [&](const string& str) {
            int len = str.length();
            vector<int> res(len, 1);
            // For each i, find max length of palindrome starting at i
            // Standard O(N^2) expansion is acceptable for N=1000, but we must ensure it covers even/odd
            for (int i = 0; i < len; ++i) {
                // Odd length
                for (int k = 0; i - k >= 0 && i + k < len; ++k) {
                    if (str[i - k] == str[i + k]) res[i - k] = max(res[i - k], 2 * k + 1);
                    else break;
                }
                // Even length
                for (int k = 0; i - k >= 0 && i + k + 1 < len; ++k) {
                    if (str[i - k] == str[i + k + 1]) res[i - k] = max(res[i - k], 2 * k + 2);
                    else break;
                }
            }
            return res;
        };

        // Helper to find longest palindrome ending at each index
        auto get_longest_ending = [&](const string& str) {
            int len = str.length();
            vector<int> res(len, 1);
            for (int i = 0; i < len; ++i) {
                for (int k = 0; i - k >= 0 && i + k < len; ++k) {
                    if (str[i - k] == str[i + k]) res[i + k] = max(res[i + k], 2 * k + 1);
                    else break;
                }
                for (int k = 0; i - k >= 0 && i + k + 1 < len; ++k) {
                    if (str[i - k] == str[i + k + 1]) res[i + k + 1] = max(res[i + k + 1], 2 * k + 2);
                    else break;
                }
            }
            return res;
        };

        vector<int> start_pal_s = get_longest_starting(s);
        vector<int> end_pal_t = get_longest_ending(t);

        int ans = 0;
        for (int x : start_pal_s) ans = max(ans, x);
        for (int x : get_longest_starting(t)) ans = max(ans, x);

        // DP[i][j]: longest matching suffix of s[0...i] and reverse prefix of t[j...m-1]
        // i.e., s[i-k+1...i] == reverse(t[j...j+k-1])
        vector<vector<int>> dp(n, vector<int>(m, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = m - 1; j >= 0; --j) {
                if (s[i] == t[j]) {
                    dp[i][j] = 1 + ((i > 0 && j < m - 1) ? dp[i - 1][j + 1] : 0);
                    int k = dp[i][j];
                    // Case 1: Palindrome A is in s, right after B
                    int pal_s = (i + 1 < n) ? start_pal_s[i + 1] : 0;
                    ans = max(ans, 2 * k + pal_s);
                    // Case 2: Palindrome A is in t, left of B^R
                    int pal_t = (j > 0) ? end_pal_t[j - 1] : 0;
                    ans = max(ans, 2 * k + pal_t);
                }
            }
        }

        return ans;
    }
};
# @lc code=end