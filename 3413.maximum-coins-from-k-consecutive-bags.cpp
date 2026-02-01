#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        sort(coins.begin(), coins.end());
        long long ans = solve(coins, k);
        
        int n = coins.size();
        vector<vector<int>> reversed_coins(n, vector<int>(3));
        for (int i = 0; i < n; ++i) {
            // Transform window ending at r_i to window starting at -r_i
            reversed_coins[i][0] = -coins[n - 1 - i][1];
            reversed_coins[i][1] = -coins[n - 1 - i][0];
            reversed_coins[i][2] = coins[n - 1 - i][2];
        }
        ans = max(ans, solve(reversed_coins, k));
        
        return ans;
    }

private:
    long long solve(const vector<vector<int>>& coins, int k) {
        int n = coins.size();
        long long max_coins = 0;
        long long current_full_sum = 0;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            long long target = (long long)coins[i][0] + k - 1;
            // Include all segments that end before or at the window target
            while (j < n && (long long)coins[j][1] <= target) {
                current_full_sum += (long long)(coins[j][1] - coins[j][0] + 1) * coins[j][2];
                j++;
            }
            
            long long current_total = current_full_sum;
            // Calculate partial overlap with the next segment if it starts before the target
            if (j < n && (long long)coins[j][0] <= target) {
                current_total += (long long)(target - coins[j][0] + 1) * coins[j][2];
            }
            max_coins = max(max_coins, current_total);
            
            // Prepare for next i: remove current segment i from the full sum
            if (j > i) {
                current_full_sum -= (long long)(coins[i][1] - coins[i][0] + 1) * coins[i][2];
            } else {
                // Window ends before the current segment ends
                j = i + 1;
                current_full_sum = 0;
            }
        }
        return max_coins;
    }
};
# @lc code=end