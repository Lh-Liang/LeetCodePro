#
# @lc app=leetcode id=3504 lang=cpp
#
# [3504] Longest Palindrome After Substring Concatenation II
#
# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        // Calculate character frequencies for both strings
        vector<int> freq_s(26, 0), freq_t(26, 0);
        for (char c : s) freq_s[c - 'a']++;
        for (char c : t) freq_t[c - 'a']++;
        
        // Compute maximum length of palindrome
        int maxLength = 0;
        bool oddCenter = false; // To allow a single odd character in the center if needed
        // Calculate pairs from both sides and check central character possibility
        for (int i = 0; i < 26; ++i) {
            int pairs = min(freq_s[i], freq_t[i]);
            maxLength += pairs * 2;
            
            if ((freq_s[i] > pairs || freq_t[i] > pairs) && !oddCenter) {
                maxLength += 1; // Allow one odd character as center of palindrome
                oddCenter = true;
            }
        }
        return maxLength;
    }
};
# @lc code=end