#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.length();
        int m = str2.length();
        int L = n + m - 1;
        string word(L, '?');
        vector<bool> fixed(L, false);

        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    if (word[i + j] != '?' && word[i + j] != str2[j]) return "";
                    word[i + j] = str2[j];
                    fixed[i + j] = true;
                }
            }
        }

        for (int i = 0; i < L; ++i) {
            if (word[i] == '?') word[i] = 'a';
        }

        auto is_match = [&](int idx) {
            if (idx < 0 || idx >= n) return false;
            for (int j = 0; j < m; ++j) {
                if (word[idx + j] != str2[j]) return false;
            }
            return true;
        };

        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'F' && is_match(i)) {
                int target = -1;
                for (int k = i + m - 1; k >= i; --k) {
                    if (!fixed[k]) {
                        target = k;
                        break;
                    }
                }

                if (target == -1) return "";

                bool solved = false;
                char original = word[target];
                for (char c = 'b'; c <= 'z'; ++c) {
                    word[target] = c;
                    if (!is_match(i)) {
                        bool conflict = false;
                        // Check if this change creates a match at any previous 'F' index
                        for (int prev = max(0, target - m + 1); prev < i; ++prev) {
                            if (str1[prev] == 'F' && is_match(prev)) {
                                conflict = true;
                                break;
                            }
                        }
                        if (!conflict) {
                            solved = true;
                            break;
                        }
                    }
                }
                if (!solved) return "";
            }
        }

        // Final verification pass
        for (int i = 0; i < n; ++i) {
            bool match = is_match(i);
            if (str1[i] == 'T' && !match) return "";
            if (str1[i] == 'F' && match) return "";
        }

        return word;
    }
};
# @lc code=end