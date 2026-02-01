#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        int n = coins.size();
        sort(coins.begin(), coins.end());
        
        long long max_coins = 0;
        
        // Case 1: Window starts at the beginning of segment i
        // Window range: [coins[i][0], coins[i][0] + k - 1]
        long long current_sum = 0;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            long long window_end = (long long)coins[i][0] + k - 1;
            // Move j to the first segment that is NOT fully contained in the window
            while (j < n && (long long)coins[j][1] <= window_end) {
                current_sum += (long long)(coins[j][1] - coins[j][0] + 1) * coins[j][2];
                j++;
            }
            
            long long total = current_sum;
            // If segment j starts before the window ends, add partial coins
            if (j < n && (long long)coins[j][0] <= window_end) {
                total += (long long)(window_end - coins[j][0] + 1) * coins[j][2];
            }
            max_coins = max(max_coins, total);
            
            // Prepare for next i: remove segment i from the 'fully contained' sum
            if (j > i) {
                current_sum -= (long long)(coins[i][1] - coins[i][0] + 1) * coins[i][2];
            } else {
                // If segment i itself was longer than k, j would be at i
                j = i + 1;
                current_sum = 0;
            }
        }
        
        // Case 2: Window ends at the end of segment i
        // Window range: [coins[i][1] - k + 1, coins[i][1]]
        current_sum = 0;
        j = 0;
        for (int i = 0; i < n; ++i) {
            long long window_start = (long long)coins[i][1] - k + 1;
            current_sum += (long long)(coins[i][1] - coins[i][0] + 1) * coins[i][2];
            
            // Move j to the first segment that is at least partially inside the window
            while (j < n && (long long)coins[j][1] < window_start) {
                current_sum -= (long long)(coins[j][1] - coins[j][0] + 1) * coins[j][2];
                j++;
            }
            
            long long total = current_sum;
            // If segment j starts before the window starts, subtract the part outside
            if (j < n && (long long)coins[j][0] < window_start) {
                total -= (long long)(window_start - coins[j][0]) * coins[j][2];
            }
            max_coins = max(max_coins, total);
        }
        
        return max_coins;
    }
};