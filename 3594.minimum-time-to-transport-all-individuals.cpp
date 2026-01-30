#
# @lc app=leetcode id=3594 lang=cpp
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        if (k == 1 && n > 1) return -1.0;

        int num_masks = 1 << n;
        vector<int> max_time(num_masks, 0);
        for (int i = 0; i < num_masks; ++i) {
            for (int j = 0; j < n; ++j) {
                if ((i >> j) & 1) {
                    max_time[i] = max(max_time[i], time[j]);
                }
            }
        }

        // dist[mask][pos][stage]
        // pos: 0 for base camp, 1 for destination
        double dist[1 << 12][2][5];
        for (int i = 0; i < num_masks; ++i) {
            for (int j = 0; j < 2; ++j) {
                for (int s = 0; s < m; ++s) {
                    dist[i][j][s] = 1e18;
                }
            }
        }

        priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> pq;
        
        dist[0][0][0] = 0.0;
        pq.push({0.0, 0}); // state: (mask << 4) | (pos << 3) | stage

        while (!pq.empty()) {
            auto [d, curr] = pq.top();
            pq.pop();

            int mask = curr >> 4;
            int pos = (curr >> 3) & 1;
            int st = curr & 7;

            if (d > dist[mask][pos][st] + 1e-11) continue;
            if (mask == num_masks - 1 && pos == 1) return d;

            if (pos == 0) { // Boat at base camp
                int base_mask = (num_masks - 1) ^ mask;
                for (int sub = base_mask; sub > 0; sub = (sub - 1) & base_mask) {
                    int cnt = __builtin_popcount(sub);
                    if (cnt >= 1 && cnt <= k) {
                        double cost = max_time[sub] * mul[st];
                        int nst = (st + (int)floor(cost + 1e-9)) % m;
                        int nmask = mask | sub;
                        if (dist[nmask][1][nst] > d + cost) {
                            dist[nmask][1][nst] = d + cost;
                            pq.push({dist[nmask][1][nst], (nmask << 4) | (1 << 3) | nst});
                        }
                    }
                }
            } else { // Boat at destination
                if (mask != num_masks - 1) {
                    for (int i = 0; i < n; ++i) {
                        if ((mask >> i) & 1) {
                            double cost = time[i] * mul[st];
                            int nst = (st + (int)floor(cost + 1e-9)) % m;
                            int nmask = mask ^ (1 << i);
                            if (dist[nmask][0][nst] > d + cost) {
                                dist[nmask][0][nst] = d + cost;
                                pq.push({dist[nmask][0][nst], (nmask << 4) | (0 << 3) | nst});
                            }
                        }
                    }
                }
            }
        }

        return -1.0;
    }
};
# @lc code=end