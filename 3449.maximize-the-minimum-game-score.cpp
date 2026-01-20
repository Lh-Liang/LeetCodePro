#
# @lc app=leetcode id=3449 lang=cpp
#
# [3449] Maximize the Minimum Game Score
#
#include <bits/stdc++.h>
using namespace std;

# @lc code=start
class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        int n = (int)points.size();
        long long mn = *min_element(points.begin(), points.end());
        long long hi = mn * 1LL * m; // safe upper bound

        auto feasible = [&](long long X) -> bool {
            if (X == 0) return true;

            auto req = [&](int i) -> long long {
                long long p = points[i];
                return (X + p - 1) / p;
            };

            long long moves = 1; // first move: -1 -> 0
            if (moves > m) return false;

            long long extra = 0; // extra landings already obtained for current i

            // process indices 0..n-3, must end each step at i+1
            for (int i = 0; i <= n - 3; i++) {
                long long have = 1 + extra;
                long long need = req(i);
                long long d = (need > have) ? (need - have) : 0; // bounces needed

                // cost of bounces: 2*d
                if (d > 0) {
                    // early overflow-safe check against m
                    if (moves + 2 * d > (long long)m) return false;
                    moves += 2 * d;
                }

                // move right once to reach i+1
                if (moves + 1 > (long long)m) return false;
                moves += 1;

                // those d bounces contribute d extra landings to i+1
                extra = d;
            }

            // Now at index n-2 (or 0 if n==2). Handle last edge (n-2, n-1).
            int i2 = n - 2;
            long long have2 = 1 + extra;
            long long need2 = req(i2);
            long long needLast = req(n - 1);

            // Option A: end at n-2 => returns = k, last landings = k
            long long kA = max(needLast, max(0LL, need2 - have2));
            long long movesA = moves + 2 * kA;

            // Option B: end at n-1 => returns = k-1, last landings = k
            long long kB = max(needLast, need2 - have2 + 1);
            long long movesB = moves + 2 * kB - 1;

            long long best = min(movesA, movesB);
            return best <= (long long)m;
        };

        long long lo = 0;
        while (lo < hi) {
            long long mid = lo + (hi - lo + 1) / 2;
            if (feasible(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
# @lc code=end
