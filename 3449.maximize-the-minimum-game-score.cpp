#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#
# @lc app=leetcode id=3449 lang=cpp
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution {
public:
    bool check(long long target, int n, const vector<int>& points, long long m) {
        long long total_moves = 0;
        long long pre_extra = 0; // additions gained from the next element's perspective

        for (int i = 0; i < n; ++i) {
            long long needed = (target + points[i] - 1) / points[i];
            long long actual = 1 + pre_extra; // 1 from the initial move to this index
            
            if (actual < needed) {
                long long diff = needed - actual;
                // To get 'diff' more points at i, we move i -> i+1 -> i 'diff' times.
                // This costs 2 * diff moves and gives 'diff' points to i+1.
                if (i == n - 1) {
                    // If it's the last element, we must move back to n-2 and forward to n-1
                    total_moves += 2 * diff;
                } else {
                    total_moves += 2 * diff;
                    pre_extra = diff;
                }
            } else {
                pre_extra = 0;
            }
            
            // Add the single move to go from i to i+1 (except for the last element)
            if (i < n - 1) total_moves++;
            
            if (total_moves > m) return false;
        }
        
        return total_moves <= m;
    }

    long long maxScore(vector<int>& points, int m) {
        int n = points.size();
        long long low = 0, high = 1e15; // Sufficiently large bound
        long long ans = 0;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (mid == 0) {
                ans = max(ans, 0LL);
                low = mid + 1;
                continue;
            }
            if (check(mid, n, points, (long long)m)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};
# @lc code=end