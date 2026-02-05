#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution {
public:
    int shortestMatchingSubstring(string s, string p) {
        // Handle special edge case
        if (p == "**") return 0;
        int n = s.size();
        int m = p.size();
        // Find star positions
        int star1 = p.find('*');
        int star2 = p.find('*', star1 + 1);
        string prefix = p.substr(0, star1);
        string middle = p.substr(star1 + 1, star2 - star1 - 1);
        string suffix = p.substr(star2 + 1);
        int minLen = n + 1;
        for (int i = 0; i + prefix.size() <= n; ++i) {
            // Check prefix
            if (s.substr(i, prefix.size()) != prefix) continue;
            int start = i + prefix.size();
            // Find middle match
            for (int j = start; j + middle.size() <= n; ++j) {
                if (s.substr(j, middle.size()) != middle) continue;
                int afterMiddle = j + middle.size();
                // Check suffix
                if (afterMiddle + suffix.size() > n) continue;
                if (s.substr(afterMiddle, suffix.size()) != suffix) continue;
                // Valid match from i to afterMiddle + suffix.size() - 1
                int len = (afterMiddle + suffix.size()) - i;
                if (len < minLen) minLen = len;
            }
        }
        return (minLen <= n) ? minLen : -1;
    }
};
# @lc code=end