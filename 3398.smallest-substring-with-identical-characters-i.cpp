#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3398 lang=cpp
 *
 * [3398] Smallest Substring With Identical Characters I
 */

// @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = (int)s.size();

        auto feasible = [&](int L) -> bool {
            const int INF = 1e9;
            vector<vector<int>> dp(2, vector<int>(L + 1, INF));

            // Initialize at position 0
            for (int c = 0; c < 2; c++) {
                char ch = (c == 0 ? '0' : '1');
                dp[c][1] = (s[0] != ch);
            }

            for (int i = 1; i < n; i++) {
                vector<vector<int>> ndp(2, vector<int>(L + 1, INF));
                for (int last = 0; last < 2; last++) {
                    for (int len = 1; len <= L; len++) {
                        int cur = dp[last][len];
                        if (cur == INF) continue;
                        for (int nc = 0; nc < 2; nc++) {
                            int nlen;
                            if (nc == last) {
                                if (len == L) continue;
                                nlen = len + 1;
                            } else {
                                nlen = 1;
                            }
                            char want = (nc == 0 ? '0' : '1');
                            int add = (s[i] != want);
                            ndp[nc][nlen] = min(ndp[nc][nlen], cur + add);
                        }
                    }
                }
                dp.swap(ndp);
            }

            int best = INT_MAX;
            for (int c = 0; c < 2; c++) {
                for (int len = 1; len <= L; len++) {
                    best = min(best, dp[c][len]);
                }
            }
            return best <= numOps;
        };

        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
// @lc code=end
