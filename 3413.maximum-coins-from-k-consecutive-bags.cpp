#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        // Sort intervals by start position
        sort(coins.begin(), coins.end());
        int n = coins.size();
        long long max_coins = 0;

        // Strategy 1: Window starts at the beginning of an interval (coins[i][0])
        // The window is [coins[i][0], coins[i][0] + k - 1]
        long long cur_sum = 0;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            long long start = coins[i][0];
            long long end = start + k - 1;

            // Expand j to include all intervals that start within the window [start, end]
            while (j < n && coins[j][0] <= end) {
                cur_sum += (long long)(coins[j][1] - coins[j][0] + 1) * coins[j][2];
                j++;
            }

            // Calculate total coins for the current window
            long long current_window_coins = cur_sum;

            // The last added interval (j-1) might extend beyond 'end'.
            // We need to subtract the part that is outside.
            if (j > 0) {
                long long overlap_end = coins[j - 1][1];
                if (overlap_end > end) {
                    current_window_coins -= (overlap_end - end) * coins[j - 1][2];
                }
            }

            max_coins = max(max_coins, current_window_coins);

            // Before moving i to i+1, remove interval i from cur_sum
            cur_sum -= (long long)(coins[i][1] - coins[i][0] + 1) * coins[i][2];
        }

        // Strategy 2: Window ends at the end of an interval (coins[j][1])
        // The window is [coins[j][1] - k + 1, coins[j][1]]
        cur_sum = 0;
        int i = 0;
        for (int l = 0; l < n; ++l) {
            long long end = coins[l][1];
            long long start = end - k + 1;
            
            // Add current interval to sum
            cur_sum += (long long)(coins[l][1] - coins[l][0] + 1) * coins[l][2];

            // Remove intervals from the left that are completely outside the window (end before 'start')
            while (i <= l && coins[i][1] < start) {
                cur_sum -= (long long)(coins[i][1] - coins[i][0] + 1) * coins[i][2];
                i++;
            }

            // Calculate total coins for the current window
            long long current_window_coins = cur_sum;

            // The first interval (i) might start before 'start'.
            // We need to subtract the part that is outside.
            if (i <= l) {
                long long overlap_start = coins[i][0];
                if (overlap_start < start) {
                    current_window_coins -= (start - overlap_start) * coins[i][2];
                }
            }

            max_coins = max(max_coins, current_window_coins);
        }

        return max_coins;
    }
};
# @lc code=end