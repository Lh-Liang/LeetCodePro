#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#
# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        vector<int> freqS(26, 0), freqT(26, 0);
        // Count frequencies of characters in both strings
        for (char c : s) ++freqS[c - 'a'];
        for (char c : t) ++freqT[c - 'a'];
        int maxLength = 0;
        bool oddFrequencyFound = false;
        // Sum pairs and detect if there's any odd frequency to add one more to result
        for (int i = 0; i < 26; ++i) {
            int totalFreq = freqS[i] + freqT[i];
            maxLength += (totalFreq / 2) * 2; // Add maximum even part
            if (totalFreq % 2 == 1) oddFrequencyFound = true;
        }
        // If there's an odd frequency, we can have a center of a palindrome
        if (oddFrequencyFound) ++maxLength;
        return maxLength;
    }
};
# @lc code=end