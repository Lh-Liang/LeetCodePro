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
        int len = n + m - 1;
        string res(len, '?');
        // Step 1: Place str2 at 'T' positions
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    int pos = i + j;
                    if (res[pos] == '?') {
                        res[pos] = str2[j];
                    } else if (res[pos] != str2[j]) {
                        return "";
                    }
                }
            }
        }
        // Step 2: Fill remaining with 'a'
        for (int i = 0; i < len; ++i) {
            if (res[i] == '?') res[i] = 'a';
        }
        // Step 3: Fix 'F' positions, ensuring 'T' constraints are preserved
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'F') {
                bool match = true;
                for (int j = 0; j < m; ++j) {
                    if (res[i + j] != str2[j]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    bool fixed = false;
                    for (int j = m - 1; j >= 0; --j) {
                        int pos = i + j;
                        if (str1.size() > pos - m + 1 && pos - m + 1 >= 0) {
                            // Check if this position is inside a 'T' window
                            bool in_T = false;
                            for (int t = max(0, pos - m + 1); t <= min(n - 1, pos); ++t) {
                                if (str1[t] == 'T' && pos - t < m) {
                                    if (str2[pos - t] != res[pos]) {
                                        in_T = true;
                                        break;
                                    }
                                }
                            }
                            if (in_T) continue;
                        }
                        // Try next lex smallest not equal to str2[j]
                        for (char c = 'a'; c <= 'z'; ++c) {
                            if (c != str2[j] && c != res[pos]) {
                                char old = res[pos];
                                res[pos] = c;
                                bool still_T_valid = true;
                                // Check all T windows covering this pos
                                for (int t = max(0, pos - m + 1); t <= min(n - 1, pos); ++t) {
                                    if (str1[t] == 'T' && pos - t < m) {
                                        if (res.substr(t, m) != str2) {
                                            still_T_valid = false;
                                            break;
                                        }
                                    }
                                }
                                if (still_T_valid) {
                                    fixed = true;
                                    break;
                                } else {
                                    res[pos] = old;
                                }
                            }
                        }
                        if (fixed) break;
                    }
                    if (!fixed) return "";
                }
            }
        }
        // Step 4: Final validation
        for (int i = 0; i < n; ++i) {
            string sub = res.substr(i, m);
            if (str1[i] == 'T' && sub != str2) return "";
            if (str1[i] == 'F' && sub == str2) return "";
        }
        return res;
    }
};
# @lc code=end