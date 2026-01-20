#
# @lc app=leetcode id=3538 lang=cpp
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        // We need to keep exactly m signs, including the first (0) and the last (n-1).
        int m = n - k;
        
        // Prefix sums for time to quickly calculate range sums.
        // P[i] stores the sum of time[0]...time[i-1].
        vector<int> P(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            P[i + 1] = P[i] + time[i];
        }

        // dp[curr][prev] stores the minimum travel time to reach the sign at index 'curr',
        // given that the immediately preceding kept sign was at index 'prev'.
        // Dimensions: n x n.
        // We initialize with a large value representing infinity.
        vector<vector<int>> dp(n, vector<int>(n, 1e9));

        // Base Case: We have selected 2 signs so far: the start (index 0) and some 'next'.
        // The 'prev' for these states is always 0.
        for (int next = 1; next < n; ++next) {
            // Segment from 0 to next.
            // Distance: position[next] - position[0]
            // Rate: time[0] (no merges happen before index 0, and 0 is kept)
            dp[next][0] = (position[next] - position[0]) * time[0];
        }

        // We iterate to select the remaining m-2 signs.
        // 'step' represents the number of signs selected so far (starting from 2).
        for (int step = 2; step < m; ++step) {
            vector<vector<int>> new_dp(n, vector<int>(n, 1e9));
            
            // 'curr' is the index of the last kept sign in the current state.
            for (int curr = 1; curr < n; ++curr) {
                // 'prev' is the index of the sign kept before 'curr'.
                for (int prev = 0; prev < curr; ++prev) {
                    if (dp[curr][prev] == 1e9) continue;

                    // Calculate the travel rate for the segment starting at 'curr'.
                    // Due to merges, the effective time at 'curr' is the sum of time[p]
                    // for all p such that prev < p <= curr.
                    // This is because all signs strictly between prev and curr are removed,
                    // and their times are accumulated into the sign at 'curr'.
                    int current_rate = P[curr + 1] - P[prev + 1];
                    
                    // Try all possible next kept signs.
                    for (int next = curr + 1; next < n; ++next) {
                        int dist = position[next] - position[curr];
                        int cost = dist * current_rate;
                        
                        if (dp[curr][prev] + cost < new_dp[next][curr]) {
                            new_dp[next][curr] = dp[curr][prev] + cost;
                        }
                    }
                }
            }
            dp = new_dp;
        }

        // The destination is always at index n-1.
        // We look for the minimum cost ending at n-1 with any valid previous sign.
        int min_total_time = 1e9;
        for (int prev = 0; prev < n - 1; ++prev) {
            min_total_time = min(min_total_time, dp[n - 1][prev]);
        }

        return min_total_time;
    }
};
# @lc code=end