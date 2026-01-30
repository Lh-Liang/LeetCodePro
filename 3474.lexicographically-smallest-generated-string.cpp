#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#
# @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.length();
        int m = str2.length();
        int len = n + m - 1;
        string res(len, ' ');
        vector<bool> fixed(len, false);

        // Phase 1: Apply 'T' constraints
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    if (fixed[i + j] && res[i + j] != str2[j]) return "";
                    res[i + j] = str2[j];
                    fixed[i + j] = true;
                }
            }
        }

        // Phase 2: Greedy fill non-fixed with 'a'
        for (int i = 0; i < len; ++i) {
            if (!fixed[i]) res[i] = 'a';
        }

        // Phase 3: Resolve 'F' constraints
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
                    bool resolved = false;
                    for (int j = m - 1; j >= 0; --j) {
                        if (!fixed[i + j]) {
                            // Change to 'b' or next char to break match
                            // Since it was 'a', if str2[j] == 'a', change to 'b'
                            // If str2[j] != 'a', it wouldn't match 'a', but here it matches
                            // so res[i+j] must equal str2[j].
                            for (char c = 'b'; c <= 'z'; ++c) {
                                if (c != str2[j]) {
                                    res[i + j] = c;
                                    resolved = true;
                                    break;
                                }
                            }
                            if (resolved) break;
                        }
                    }
                    if (!resolved) return "";
                }
            }
        }

        // Final verification for 'F' constraints (needed due to potential overlaps)
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'F') {
                bool match = true;
                for (int j = 0; j < m; ++j) {
                    if (res[i + j] != str2[j]) {
                        match = false;
                        break;
                    }
                }
                if (match) return "";
            }
        }

        return res;
    }
};
# @lc code=end