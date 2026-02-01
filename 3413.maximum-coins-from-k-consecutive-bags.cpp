#include <vector>
#include <algorithm>

using namespace std;

/*
 * @lc app=leetcode id=3413 lang=cpp
 *
 * [3413] Maximum Coins From K Consecutive Bags
 */

// @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        int n = coins.size();
        sort(coins.begin(), coins.end());

        long long max_coins = 0;

        // Case 1: Window starts at the beginning of coins[i]
        // Window range: [coins[i][0], coins[i][0] + k - 1]
        long long current_sum = 0;
        int right = 0;
        for (int left = 0; left < n; ++left) {
            long long window_end = (long long)coins[left][0] + k - 1;
            
            // Add segments that are completely within the window
            while (right < n && (long long)coins[right][1] <= window_end) {
                current_sum += (long long)(coins[right][1] - coins[right][0] + 1) * coins[right][2];
                right++;
            }
            
            long long total = current_sum;
            // Add partial segment if the window end falls inside the next segment
            if (right < n && (long long)coins[right][0] <= window_end) {
                total += (long long)(window_end - coins[right][0] + 1) * coins[right][2];
            }
            max_coins = max(max_coins, total);

            // Prepare current_sum for next left pointer increment
            if (right > left) {
                current_sum -= (long long)(coins[left][1] - coins[left][0] + 1) * coins[left][2];
            } else {
                right = left + 1;
                current_sum = 0;
            }
        }

        // Case 2: Window ends at the end of coins[i]
        // Window range: [coins[i][1] - k + 1, coins[i][1]]
        current_sum = 0;
        int left_ptr = 0;
        for (int right_idx = 0; right_idx < n; ++right_idx) {
            current_sum += (long long)(coins[right_idx][1] - coins[right_idx][0] + 1) * coins[right_idx][2];
            long long window_start = (long long)coins[right_idx][1] - k + 1;
            
            // Remove segments that are completely outside the window (to the left)
            while (left_ptr < n && (long long)coins[left_ptr][1] < window_start) {
                current_sum -= (long long)(coins[left_ptr][1] - coins[left_ptr][0] + 1) * coins[left_ptr][2];
                left_ptr++;
            }
            
            long long total = current_sum;
            // Subtract partial segment if the window start falls inside the first segment in range
            if (left_ptr <= right_idx && (long long)coins[left_ptr][0] < window_start) {
                total -= (long long)(window_start - coins[left_ptr][0]) * coins[left_ptr][2];
            }
            max_coins = max(max_coins, total);
        }

        return max_coins;
    }
};
// @lc code=end