#
# @lc app=leetcode id=3538 lang=cpp
#
# [3538] Merge Operations for Minimum Travel Time
#
# @lc code=start
class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        const int INF = 1e9;
        const int maxA = 101;  // sum of time can be up to 100
        
        // Precompute prefix sums of time
        vector<int> prefixTime(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixTime[i + 1] = prefixTime[i] + time[i];
        }
        
        // dp[i][r][a] = min travel time to reach sign i (kept), having removed r signs,
        // with accumulated time a at sign i
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(k + 1, vector<int>(maxA, INF)));
        
        dp[0][0][time[0]] = 0;
        
        for (int i = 1; i < n; i++) {
            for (int prev = 0; prev < i; prev++) {
                int removed = i - prev - 1;  // signs removed between prev and i
                if (removed > k) continue;
                
                // Accumulated time at sign i: sum of time[t] for prev < t <= i
                int acc_i = prefixTime[i + 1] - prefixTime[prev + 1];
                
                for (int r = removed; r <= k; r++) {
                    int r_prev = r - removed;
                    
                    for (int a = 1; a < maxA; a++) {
                        if (dp[prev][r_prev][a] == INF) continue;
                        
                        // Travel from prev to i using rate a (accumulated time at prev)
                        int dist = position[i] - position[prev];
                        int travel = dist * a;
                        int new_cost = dp[prev][r_prev][a] + travel;
                        dp[i][r][acc_i] = min(dp[i][r][acc_i], new_cost);
                    }
                }
            }
        }
        
        int ans = INF;
        for (int a = 1; a < maxA; a++) {
            ans = min(ans, dp[n-1][k][a]);
        }
        return ans;
    }
};
# @lc code=end