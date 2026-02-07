#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        // Initialize result with smallest character for lexicographic priority
        string result(n + m - 1, 'a');
        vector<bool> placed(n + m - 1, false);
        
        // Place str2 where required by 'T', checking for conflicts with 'F'
        for (int i = 0; i <= n - m; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    if (placed[i + j] && result[i + j] != str2[j]) return "";
                    result[i + j] = str2[j];
                    placed[i + j] = true;
                }
            }
        }

        // Fill remaining with smallest lexicographical order while respecting 'F'
        for (int i = 0; i <= n + m - 2; ++i) {
            if (!placed[i]) {
                result[i] = 'a';
            }
        }

        // Ensure no formation under 'F' constraints at construction time
        for (int i = 0; i <= n - m; ++i) {
            if (str1[i] == 'F') {
                bool matches = true;
                for (int j = 0; j < m && matches; ++j) {
                    if (result[i + j] != str2[j]) {
                        matches = false;
                    }
                }
                if (matches) return "";
            }
        }

        return result;
    }
};
# @lc code=end