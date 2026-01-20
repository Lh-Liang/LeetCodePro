#
# @lc app=leetcode id=3504 lang=cpp
#
# [3504] Longest Palindrome After Substring Concatenation II
#
# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        // We need to check two cases:
        // 1. The center of the palindrome is within the substring from s.
        // 2. The center of the palindrome is within the substring from t.
        // The second case is symmetric to the first if we swap s and t.
        return max(solve(s, t), solve(t, s));
    }

private:
    // Solves the problem assuming the center of the palindrome is in s (or at the boundary)
    int solve(const string& s, const string& t) {
        int n = s.length();
        int m = t.length();
        string tr = t;
        reverse(tr.begin(), tr.end());

        // dp[i][j] stores the length of the longest common suffix 
        // of s[0...i-1] and tr[0...j-1].
        // This effectively finds the longest suffix of s[0...i-1] that matches a suffix of tr[0...j-1].
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        
        // match_s[i] stores the maximum length of a suffix of s[0...i-1]
        // that appears as a substring in tr (which is t reversed).
        // This corresponds to finding the longest P such that P is a suffix of s[0...i-1]
        // and P^R is a substring of t.
        vector<int> match_s(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (s[i - 1] == tr[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = 0;
                }
                match_s[i] = max(match_s[i], dp[i][j]);
            }
        }

        int max_len = 0;

        // Case 1: The palindrome center is exactly at the concatenation boundary.
        // This means A = P and B = P^R. Length is 2 * |P|.
        // P is a suffix of some prefix of s (i.e., a substring ending at some i).
        // P^R must be in t. This is exactly what match_s[i] computes.
        for (int i = 0; i <= n; ++i) {
            max_len = max(max_len, 2 * match_s[i]);
        }

        // Case 2: The palindrome center is inside s.
        // We iterate over all possible centers in s.
        for (int i = 0; i < n; ++i) {
            // Odd length palindrome centered at s[i]
            int l = i, r = i;
            while (l >= 0 && r < n && s[l] == s[r]) {
                l--;
                r++;
            }
            // The maximal palindrome in s centered at i is s[l+1 ... r-1].
            // Its length is (r - 1) - (l + 1) + 1 = r - l - 1.
            // The part of s to the left of this palindrome ends at index l.
            // We can extend this palindrome by P if P is a suffix of s[...l] and P^R is in t.
            int pal_len = r - l - 1;
            int p_len = match_s[l + 1]; // match_s is 1-based size, so index l+1 corresponds to prefix length l+1
            max_len = max(max_len, pal_len + 2 * p_len);

            // Even length palindrome centered between s[i] and s[i+1]
            l = i;
            r = i + 1;
            while (l >= 0 && r < n && s[l] == s[r]) {
                l--;
                r++;
            }
            // Palindrome s[l+1 ... r-1]
            pal_len = r - l - 1;
            if (pal_len > 0) {
                 p_len = match_s[l + 1];
                 max_len = max(max_len, pal_len + 2 * p_len);
            }
        }

        return max_len;
    }
};
# @lc code=end