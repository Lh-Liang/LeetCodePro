#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#
# @lc code=start
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size();
        int m = str2.size();
        string result(n + m - 1, 'z'); // Start with max lexicographical string
        for (int i = 0; i <= n - m; ++i) {
            // Try placing str2 at position i if allowed by str1
            if (str1[i] == 'T') {
                result.replace(i, m, str2); // Place str2 here
            } else {
                // Place smallest characters that don't match str2 exactly here
                for (int j = 0; j < m; ++j) {
                    result[i + j] = std::min(result[i + j], (char)(str2[j] + 1)); // Ensure it's different than str2's char
                }
            }
        }
        return result; // Return constructed lexicographically smallest string
    }
}; # @lc code=end