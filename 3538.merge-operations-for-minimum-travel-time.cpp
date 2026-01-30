#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        // dp[i][j][rem]: min time to reach sign i, 
        // where sign j was the one kept before i,
        // and rem signs have been removed in total.
        long long INF = 1e18;
        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(n, vector<long long>(k + 1, INF)));

        // Prefix sums for time to calculate segment speeds quickly
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + time[i];
        }

        // Base cases: First segment starting from position[0]
        // We keep sign 0, then the next sign we keep is i.
        // All signs between 0 and i are removed (i-1 signs).
        for (int i = 1; i < n; ++i) {
            int removed = i - 1;
            if (removed <= k) {
                dp[i][0][removed] = (long long)(position[i] - position[0]) * time[0];
            }
        }

        // DP transitions
        for (int i = 1; i < n; ++i) { // current sign index
            for (int j = 0; j < i; ++j) { // previous sign index
                for (int rem = 0; rem <= k; ++rem) { // total removed signs
                    if (dp[i][j][rem] == INF) continue;

                    // Choose the next sign to keep
                    for (int next_i = i + 1; next_i < n; ++next_i) {
                        int newly_removed = next_i - i - 1;
                        if (rem + newly_removed <= k) {
                            // Speed for segment [pos[i], pos[next_i]] is sum(time[j+1...i])
                            long long speed = pref[i + 1] - pref[j + 1];
                            long long cost = (long long)(position[next_i] - position[i]) * speed;
                            if (dp[i][j][rem] + cost < dp[next_i][i][rem + newly_removed]) {
                                dp[next_i][i][rem + newly_removed] = dp[i][j][rem] + cost;
                            }
                        }
                    }
                }
            }
        }

        // The answer is the minimum value at the final sign (n-1) with exactly k removals
        long long ans = INF;
        for (int j = 0; j < n - 1; ++j) {
            ans = min(ans, dp[n - 1][j][k]);
        }

        return (int)ans;
    }
};