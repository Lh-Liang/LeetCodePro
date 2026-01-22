#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution {
public:
    bool isPalindrome(const string& str) {
        int n = str.size();
        for (int i = 0; i < n / 2; i++) {
            if (str[i] != str[n - 1 - i]) return false;
        }
        return true;
    }
    
    int longestPalindrome(string s, string t) {
        int n = s.size(), m = t.size();
        int maxLen = 0;
        
        // Iterate through all substrings of s (including empty)
        for (int i = 0; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                // Iterate through all substrings of t (including empty)
                for (int k = 0; k <= m; k++) {
                    for (int l = k; l <= m; l++) {
                        string combined = s.substr(i, j - i) + t.substr(k, l - k);
                        if (!combined.empty() && isPalindrome(combined)) {
                            maxLen = max(maxLen, (int)combined.size());
                        }
                    }
                }
            }
        }
        
        return maxLen;
    }
};
# @lc code=end