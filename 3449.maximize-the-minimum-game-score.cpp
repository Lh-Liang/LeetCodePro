#
# @lc app=leetcode id=3449 lang=cpp
#
# [3449] Maximize the Minimum Game Score
#
# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        int n = (int)points.size();
        long long mm = (long long)m;

        long long mx = 0;
        for (int x : points) mx = max(mx, (long long)x);
        long long lo = 0, hi = mx * mm;

        auto feasible = [&](long long X) -> bool {
            if (X == 0) return true;

            // need[i] = ceil(X / points[i])
            vector<long long> need(n);
            for (int i = 0; i < n; i++) {
                need[i] = (X + points[i] - 1LL) / points[i];
            }

            // First move: -1 -> 0
            long long moves = 1;
            if (moves > mm) return false;

            long long have_i = 1;     // visits at current index i
            long long have_next = 0;  // visits already accumulated for i+1 (from bounces)

            // Process indices 0..n-3, ending at n-2
            for (int i = 0; i <= n - 3; i++) {
                // Move i -> i+1
                moves += 1;
                have_next += 1;
                if (moves > mm) return false;

                // Ensure index i meets need[i] using round trips via (i, i+1)
                if (have_i < need[i]) {
                    long long extra = need[i] - have_i;
                    // each extra requires (i+1 -> i -> i+1): 2 moves
                    moves += 2LL * extra;
                    have_i += extra;
                    have_next += extra;
                    if (moves > mm) return false;
                }

                // Advance window: now current index becomes i+1
                have_i = have_next;
                have_next = 0;
            }

            // Now current is index n-2 with visits have_i
            // Handle last edge (n-2, n-1)
            long long a0 = have_i;
            long long need_left = need[n - 2];
            long long need_right = need[n - 1];

            // After one move to n-1, n-1 has 1 visit.
            long long A = need_right - 1;      // extra full trips needed for n-1
            long long B = need_left - a0;      // extra contributions needed for n-2

            // Option 1: end at n-1
            long long T1 = max({0LL, A, B});
            long long add1 = 1 + 2LL * T1;     // move to n-1 + T1 full trips

            // Option 2: end at n-2 (final step from n-1 -> n-2 gives one more to n-2)
            long long T2 = max({0LL, A, B - 1});
            long long add2 = 2 + 2LL * T2;     // move to n-1 + T2 full trips + final move back

            moves += min(add1, add2);
            return moves <= mm;
        };

        while (lo < hi) {
            long long mid = lo + (hi - lo + 1) / 2;
            if (feasible(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
# @lc code=end
