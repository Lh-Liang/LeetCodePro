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
        int len_ = n + m - 1;
        string s(len_, '#');
        // Apply 'T' constraints
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    int pos = i + j;
                    if (s[pos] != '#' && s[pos] != str2[j]) {
                        return "";
                    }
                    s[pos] = str2[j];
                }
            }
        }
        // Fill left to right
        for (int k = 0; k < len_; ++k) {
            int i = k - m + 1;
            bool has_f = (i >= 0 && i < n && str1[i] == 'F');
            if (s[k] != '#') {
                // Fixed: check if completes 'F' window
                if (has_f) {
                    bool match = true;
                    for (int j = 0; j < m; ++j) {
                        if (s[i + j] != str2[j]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        return "";
                    }
                }
            } else {
                // Free: choose smallest valid
                bool prefix_match = false;
                if (has_f) {
                    prefix_match = true;
                    for (int j = 0; j < m - 1; ++j) {
                        int p = i + j;
                        if (s[p] != str2[j]) {
                            prefix_match = false;
                            break;
                        }
                    }
                }
                char c;
                if (!has_f || !prefix_match) {
                    c = 'a';
                } else {
                    char forb = str2[m - 1];
                    c = (forb == 'a' ? 'b' : 'a');
                }
                s[k] = c;
            }
        }
        return s;
    }
};
# @lc code=end
