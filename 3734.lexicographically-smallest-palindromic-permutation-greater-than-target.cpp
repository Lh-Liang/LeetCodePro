#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        
        // Count frequencies
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        // Check if palindrome is possible
        int oddCount = 0;
        char oddChar = '\0';
        for (auto& [ch, count] : freq) {
            if (count % 2 == 1) {
                oddCount++;
                oddChar = ch;
            }
        }
        
        if (oddCount > 1) return "";
        
        int half = n / 2;
        
        // Collect characters for the first half
        vector<char> chars;
        for (auto& [ch, count] : freq) {
            for (int i = 0; i < count / 2; i++) {
                chars.push_back(ch);
            }
        }
        sort(chars.begin(), chars.end());
        
        // Try all permutations of the first half
        do {
            string palindrome = "";
            for (int i = 0; i < half; i++) {
                palindrome += chars[i];
            }
            if (n % 2 == 1) {
                palindrome += oddChar;
            }
            for (int i = half - 1; i >= 0; i--) {
                palindrome += chars[i];
            }
            
            if (palindrome > target) {
                return palindrome;
            }
        } while (next_permutation(chars.begin(), chars.end()));
        
        return "";
    }
};
# @lc code=end