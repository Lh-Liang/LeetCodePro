#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countSubstrings(string s) {
        // dp[d][r]: count of substrings ending at previous position with remainder r mod d
        vector<long long> dp[10], ndp[10];
        for (int d = 1; d <= 9; ++d) {
            dp[d].assign(d, 0);
            ndp[d].assign(d, 0);
        }

        long long ans = 0;

        for (char ch : s) {
            int x = ch - '0';
            for (int d = 1; d <= 9; ++d) {
                fill(ndp[d].begin(), ndp[d].end(), 0);

                for (int r = 0; r < d; ++r) {
                    if (dp[d][r] == 0) continue;
                    int nr = (r * 10 + x) % d;
                    ndp[d][nr] += dp[d][r];
                }

                ndp[d][x % d] += 1; // start new substring at current position

                dp[d].swap(ndp[d]);

                if (x != 0 && d == x) {
                    ans += dp[d][0];
                }
            }
        }

        return ans;
    }
};
# @lc code=end
