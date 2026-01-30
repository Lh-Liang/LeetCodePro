#include <vector>
#include <algorithm>

using namespace std;

//
// @lc app=leetcode id=3413 lang=cpp
//
// [3413] Maximum Coins From K Consecutive Bags
//

// @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        int n = coins.size();
        sort(coins.begin(), coins.end());

        auto solve = [&](const vector<vector<int>>& segments) {
            long long max_coins = 0;
            long long current_sum = 0;
            int right = 0;

            for (int left = 0; left < n; ++left) {
                // Ensure right pointer is at least at left
                if (right < left) {
                    right = left;
                    current_sum = 0;
                }

                long long window_start = segments[left][0];
                long long window_end = window_start + k - 1;

                // Add segments that are fully contained within [window_start, window_end]
                while (right < n && (long long)segments[right][1] <= window_end) {
                    current_sum += (long long)(segments[right][1] - segments[right][0] + 1) * segments[right][2];
                    right++;
                }

                long long total = current_sum;
                // If there's a next segment, it might partially overlap with the end of the window
                if (right < n && (long long)segments[right][0] <= window_end) {
                    long long partial_len = window_end - (long long)segments[right][0] + 1;
                    total += partial_len * segments[right][2];
                }
                
                max_coins = max(max_coins, total);

                // Subtract the current left segment as the window slides forward
                if (right > left) {
                    current_sum -= (long long)(segments[left][1] - segments[left][0] + 1) * segments[left][2];
                }
            }
            return max_coins;
        };

        // Case 1: Window starts at the beginning of a segment
        long long ans = solve(coins);

        // Case 2: Window ends at the end of a segment
        // Transform segments to use the same logic: [l, r] -> [-r, -l]
        vector<vector<int>> reversed_coins = coins;
        for (int i = 0; i < n; ++i) {
            int l = reversed_coins[i][0];
            int r = reversed_coins[i][1];
            reversed_coins[i][0] = -r;
            reversed_coins[i][1] = -l;
        }
        sort(reversed_coins.begin(), reversed_coins.end());
        ans = max(ans, solve(reversed_coins));

        return ans;
    }
};
// @lc code=end