#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        const long long INF = (long long)4e18;

        // prefix sums of time
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + time[i];

        auto sumTimeInclusive = [&](int L, int R) -> long long {
            // sum time[L..R], assumes 0<=L<=R<n
            return pref[R + 1] - pref[L];
        };

        // dp[del][i][j]
        vector<vector<vector<long long>>> dp(k + 1,
            vector<vector<long long>>(n, vector<long long>(n, INF)));

        // Initialize: survivors are (0, j)
        for (int j = 1; j < n; j++) {
            int del = j - 1; // removed signs 1..j-1
            if (del <= k) {
                dp[del][0][j] = 1LL * (position[j] - position[0]) * time[0];
            }
        }

        for (int del = 0; del <= k; del++) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    long long cur = dp[del][i][j];
                    if (cur >= INF) continue;

                    // try next survivor z
                    for (int z = j + 1; z < n; z++) {
                        int gap = z - j - 1; // number of deleted signs between j and z
                        int nd = del + gap;
                        if (nd > k) continue;

                        // accumulated time at j is sum(time[i+1..j])
                        long long accJ = sumTimeInclusive(i + 1, j);
                        long long addCost = 1LL * (position[z] - position[j]) * accJ;
                        dp[nd][j][z] = min(dp[nd][j][z], cur + addCost);
                    }
                }
            }
        }

        long long ans = INF;
        for (int i = 0; i < n - 1; i++) {
            ans = min(ans, dp[k][i][n - 1]);
        }
        return (int)ans;
    }
};
// @lc code=end
