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
        string t_rev = t;
        reverse(t_rev.begin(), t_rev.end());
        
        // Compute isPalin for s
        vector<vector<bool>> isPalin_s(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) isPalin_s[i][i] = true;
        for (int i = 0; i < n - 1; i++) isPalin_s[i][i+1] = (s[i] == s[i+1]);
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                isPalin_s[i][j] = (s[i] == s[j]) && isPalin_s[i+1][j-1];
            }
        }
        
        // Compute isPalin for t_rev
        vector<vector<bool>> isPalin_t_rev(m, vector<bool>(m, false));
        for (int i = 0; i < m; i++) isPalin_t_rev[i][i] = true;
        for (int i = 0; i < m - 1; i++) isPalin_t_rev[i][i+1] = (t_rev[i] == t_rev[i+1]);
        for (int len = 3; len <= m; len++) {
            for (int i = 0; i <= m - len; i++) {
                int j = i + len - 1;
                isPalin_t_rev[i][j] = (t_rev[i] == t_rev[j]) && isPalin_t_rev[i+1][j-1];
            }
        }
        
        // Compute maxPalinStarting for s
        vector<int> maxPalinStarting_s(n + 1, 0);
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j >= i; j--) {
                if (isPalin_s[i][j]) {
                    maxPalinStarting_s[i] = j - i + 1;
                    break;
                }
            }
        }
        
        // Compute maxPalinStarting for t_rev
        vector<int> maxPalinStarting_t_rev(m + 1, 0);
        for (int i = 0; i < m; i++) {
            for (int j = m - 1; j >= i; j--) {
                if (isPalin_t_rev[i][j]) {
                    maxPalinStarting_t_rev[i] = j - i + 1;
                    break;
                }
            }
        }
        
        // Compute LCP matrix
        vector<vector<int>> lcp(n + 1, vector<int>(m + 1, 0));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (s[i] == t_rev[j]) {
                    lcp[i][j] = 1 + lcp[i+1][j+1];
                }
            }
        }
        
        int ans = 1;
        
        // Palindrome entirely in s
        for (int i = 0; i < n; i++) {
            ans = max(ans, maxPalinStarting_s[i]);
        }
        
        // Palindrome entirely in t
        for (int i = 0; i < m; i++) {
            ans = max(ans, maxPalinStarting_t_rev[i]);
        }
        
        // Combined case
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int match = lcp[i][j];
                if (match > 0) {
                    ans = max(ans, 2 * match);
                    if (i + match < n) {
                        ans = max(ans, 2 * match + maxPalinStarting_s[i + match]);
                    }
                    if (j + match < m) {
                        ans = max(ans, 2 * match + maxPalinStarting_t_rev[j + match]);
                    }
                }
            }
        }
        
        return ans;
    }
};
# @lc code=end