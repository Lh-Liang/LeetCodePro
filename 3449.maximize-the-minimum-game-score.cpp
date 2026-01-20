#
# @lc app=leetcode id=3449 lang=cpp
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    bool check(long long X, int n, const vector<int>& points, long long m) {
        if (X == 0) return true;
        
        long long total_moves = 0;
        long long extra_next = 0;
        
        for (int i = 0; i < n; ++i) {
            long long needed = (X + points[i] - 1) / points[i];
            long long current_visits = extra_next + 1; // 1 move to reach index i from i-1
            total_moves++; 
            
            if (total_moves > m) return false;
            
            if (current_visits < needed) {
                long long diff = needed - current_visits;
                // Toggle between i and i+1 to get 'diff' more visits at index i.
                // Each toggle (i -> i+1 -> i) costs 2 moves and adds 1 visit to i and i+1.
                total_moves += 2 * diff;
                extra_next = diff;
            } else {
                extra_next = 0;
            }
            
            if (total_moves > m) return false;
            
            // If we are at index n-2 and the toggles have already satisfied index n-1,
            // we don't need to move to index n-1.
            if (i == n - 2) {
                long long next_needed = (X + points[i + 1] - 1) / points[i + 1];
                if (extra_next >= next_needed) return true;
            }
        }
        
        return total_moves <= m;
    }

    long long maxScore(vector<int>& points, int m) {
        int n = points.size();
        long long low = 0;
        long long high = 1e15; // Sufficiently large upper bound
        long long ans = 0;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
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