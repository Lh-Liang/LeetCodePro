#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string lexicographicallySmallestString(string s) {
        int n = s.length();
        // cv[i][j] is true if substring s[i...j-1] can be fully removed
        vector<vector<bool>> cv(n + 1, vector<bool>(n + 1, false));

        for (int i = 0; i <= n; ++i) {
            cv[i][i] = true;
        }

        auto is_consecutive = [](char a, char b) {
            int diff = abs(a - b);
            return diff == 1 || diff == 25;
        };

        // Range DP to find all vanishable substrings
        for (int len = 2; len <= n; len += 2) {
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len;
                for (int k = i + 1; k < j; k += 2) {
                    if (is_consecutive(s[i], s[k]) && cv[i + 1][k] && cv[k + 1][j]) {
                        cv[i][j] = true;
                        break;
                    }
                }
            }
        }

        // dp[i] stores the lexicographically smallest string from suffix s[i...n-1]
        vector<string> dp(n + 1);
        dp[n] = "";

        for (int i = n - 1; i >= 0; --i) {
            // Option 1: Keep s[i] and potentially remove a vanishable block after it
            string best_suffix = "{"; // Larger than any possible string
            for (int j = i + 1; j <= n; ++j) {
                if (cv[i + 1][j]) {
                    if (dp[j] < best_suffix) {
                        best_suffix = dp[j];
                    }
                }
            }
            string opt_keep = s[i] + best_suffix;

            // Option 2: Remove s[i] as part of a vanishable block s[i...j-1]
            string opt_remove = "{";
            for (int j = i + 2; j <= n; j += 2) {
                if (cv[i][j]) {
                    if (dp[j] < opt_remove) {
                        opt_remove = dp[j];
                    }
                }
            }

            if (opt_remove < opt_keep) {
                dp[i] = opt_remove;
            } else {
                dp[i] = opt_keep;
            }
        }

        return dp[0];
    }
};
# @lc code=end