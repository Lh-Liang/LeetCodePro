#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3448 lang=cpp
 *
 * [3448] Count Substrings Divisible By Last Digit
 */

// @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        // dp[d][r] for d in 1..9, r in 0..d-1 (we allocate 0..8 for convenience)
        long long dp[10][9];
        memset(dp, 0, sizeof(dp));

        long long ans = 0;
        for (char ch : s) {
            int x = ch - '0';

            for (int d = 1; d <= 9; ++d) {
                long long ndp[9] = {0};

                for (int r = 0; r < d; ++r) {
                    if (dp[d][r] == 0) continue;
                    int nr = (r * 10 + x) % d;
                    ndp[nr] += dp[d][r];
                }

                // start new substring at this position
                ndp[x % d] += 1;

                for (int r = 0; r < d; ++r) dp[d][r] = ndp[r];
            }

            if (x != 0) ans += dp[x][0];
        }
        return ans;
    }
};
// @lc code=end
