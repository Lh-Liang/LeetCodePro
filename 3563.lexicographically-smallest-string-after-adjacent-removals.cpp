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
        
        auto is_consecutive = [](char a, char b) {
            int diff = abs(a - b);
            return diff == 1 || diff == 25;
        };

        // can_empty[i][j] is true if s[i...j] can be completely removed
        vector<vector<bool>> can_empty(n + 1, vector<bool>(n + 1, false));
        for (int i = 0; i <= n; ++i) {
            can_empty[i][i - 1] = true; // Base case: empty range
        }

        for (int len = 2; len <= n; len += 2) {
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len - 1;
                for (int k = i + 1; k <= j; k += 2) {
                    if (is_consecutive(s[i], s[k]) && can_empty[i + 1][k - 1] && can_empty[k + 1][j]) {
                        can_empty[i][j] = true;
                        break;
                    }
                }
            }
        }

        // dp[i] is the lexicographically smallest string from s[i...n-1]
        vector<string> dp(n + 1);
        dp[n] = "";

        for (int i = n - 1; i >= 0; --i) {
            // Option 1: Keep current character s[i]
            dp[i] = s[i] + dp[i + 1];

            // Option 2: Remove s[i] by pairing it with some s[k]
            for (int k = i + 1; k < n; ++k) {
                // To remove s[i] and s[k], the segment between them must be removable
                if (is_consecutive(s[i], s[k]) && can_empty[i + 1][k - 1]) {
                    if (dp[k + 1] < dp[i]) {
                        dp[i] = dp[k + 1];
                    }
                }
            }
        }

        return dp[0];
    }
};
# @lc code=end