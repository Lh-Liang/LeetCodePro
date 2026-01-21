#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int maxLen = 0;
        int n = s.length(), m = t.length();
        
        for (int i = 0; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                for (int k = 0; k <= m; k++) {
                    for (int l = k; l <= m; l++) {
                        int sLen = j - i;
                        int tLen = l - k;
                        int totalLen = sLen + tLen;
                        
                        if (totalLen <= maxLen) continue;
                        
                        bool valid = true;
                        for (int p = 0; p < totalLen / 2 && valid; p++) {
                            int left = p;
                            int right = totalLen - 1 - p;
                            
                            char charLeft = (left < sLen) ? s[i + left] : t[k + left - sLen];
                            char charRight = (right < sLen) ? s[i + right] : t[k + right - sLen];
                            
                            if (charLeft != charRight) valid = false;
                        }
                        
                        if (valid) maxLen = totalLen;
                    }
                }
            }
        }
        
        return maxLen;
    }
};
# @lc code=end