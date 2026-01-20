#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        // dp[i][j][s] is the minimum travel time from 0 to position[i]
        // where we have kept j signs (including 0 and i)
        // and s is the sum of 'pushed' time values added to the speed of the segment ending at position[i].
        // The number of merges performed is (i + 1) - j.
        // We need exactly k merges, so (n - 1 + 1) - j_final = k => j_final = n - k.
        
        int sum_time = 0;
        for (int t : time) sum_time += t;
        
        // dp[current_sign_idx][signs_kept][pushed_time_sum]
        static int dp[51][51][101];
        memset(dp, 0x3f, sizeof(dp));
        int INF = dp[0][0][0];

        // Base case: at sign 0, we have kept 1 sign, pushed time is 0 (no segment ends at 0).
        dp[0][1][0] = 0;

        for (int i = 0; i < n - 1; ++i) {
            for (int j = 1; j <= i + 1; ++j) {
                for (int s = 0; s <= sum_time; ++s) {
                    if (dp[i][j][s] == INF) continue;

                    // Option 1: Keep the next sign (i + 1)
                    // The segment [position[i], position[i+1]] will have speed (time[i] + s).
                    int next_s_keep = 0;
                    int next_time_keep = dp[i][j][s] + (position[i+1] - position[i]) * (time[i] + s);
                    if (next_time_keep < dp[i+1][j+1][next_s_keep]) {
                        dp[i+1][j+1][next_s_keep] = next_time_keep;
                    }

                    // Option 2: Remove the next sign (i + 1) (if it's not the last sign)
                    if (i + 1 < n - 1) {
                        int next_s_remove = s + time[i];
                        int next_time_remove = dp[i][j][s] + (position[i+1] - position[i]) * (time[i] + s);
                        if (next_s_remove <= sum_time && next_time_remove < dp[i+1][j][next_s_remove]) {
                            dp[i+1][j][next_s_remove] = next_time_remove;
                        }
                    }
                }
            }
        }

        // The result is dp[n-1][n-k][0]
        return dp[n - 1][n - k][0];
    }
};