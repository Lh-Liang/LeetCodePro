#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        unordered_map<char, int> charCount;
        for (char c : s) charCount[c]++;
        
        char oddChar = 0;
        int oddCount = 0;
        for (auto &[c, count] : charCount) {
            if (count % 2 != 0) {
                oddChar = c;
                oddCount++;
            }
        }
        
        if ((oddCount > 1) || (oddCount == 1 && n % 2 == 0)) return "";

        vector<char> halfPalindrome;
        for (auto &[c, count] : charCount) {
            halfPalindrome.insert(halfPalindrome.end(), count / 2, c);
        }

        sort(halfPalindrome.begin(), halfPalindrome.end());
        string bestPalindrome = "";

        do {
            string halfStr(halfPalindrome.begin(), halfPalindrome.end());
            string fullPalindrome = halfStr;
            if (oddCount == 1) fullPalindrome += oddChar;
            reverse(halfStr.begin(), halfStr.end());
            fullPalindrome += halfStr;
            if (fullPalindrome > target && (bestPalindrome.empty() || fullPalindrome < bestPalindrome)) {
                bestPalindrome = fullPalindrome;
            }
        } while (next_permutation(halfPalindrome.begin(), halfPalindrome.end()));

        return bestPalindrome;
    }
};
# @lc code=end