#
# @lc app=leetcode id=3504 lang=java
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution {
    // Helper to find the longest palindrome in a single string
    private int longestPalindromeSingle(String str) {
        int n = str.length(), maxLen = 0;
        for (int center = 0; center < n; ++center) {
            // Odd length
            int l = center, r = center;
            while (l >= 0 && r < n && str.charAt(l) == str.charAt(r)) {
                maxLen = Math.max(maxLen, r - l + 1);
                l--; r++;
            }
            // Even length
            l = center; r = center + 1;
            while (l >= 0 && r < n && str.charAt(l) == str.charAt(r)) {
                maxLen = Math.max(maxLen, r - l + 1);
                l--; r++;
            }
        }
        return maxLen;
    }
    
    public int longestPalindrome(String s, String t) {
        int maxLen = 0;
        // Case 1: Palindrome fully in s
        maxLen = Math.max(maxLen, longestPalindromeSingle(s));
        // Case 2: Palindrome fully in t
        maxLen = Math.max(maxLen, longestPalindromeSingle(t));

        // Case 3: Palindrome crossing the boundary
        int n = s.length(), m = t.length();
        // For every possible split (i in s, j in t), expand around boundary
        // Center between s[i] and t[j]
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= m; ++j) {
                // Odd length: center exactly at the boundary
                int l = i - 1, r = j;
                int len = 0;
                while (l >= 0 && r < m && s.charAt(l) == t.charAt(r)) {
                    len += 2; l--; r++;
                }
                maxLen = Math.max(maxLen, len);
                // Even length: center between s[i-1] and t[j]
                // (already handled above, since even/odd is symmetric across boundary)
            }
        }
        // Additionally, single chars at the boundary can form palindromes of len 1
        return Math.max(maxLen, 1);
    }
}
# @lc code=end