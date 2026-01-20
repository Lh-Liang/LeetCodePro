#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        if (k == 1 && n > 1) return -1.0;

        int full_mask = (1 << n) - 1;
        vector<int> max_time(1 << n, 0);
        for (int i = 0; i < (1 << n); ++i) {
            for (int j = 0; j < n; ++j) {
                if ((i >> j) & 1) {
                    max_time[i] = max(max_time[i], time[j]);
                }
            }
        }

        vector<int> subsets;
        for (int i = 1; i < (1 << n); ++i) {
            if (__builtin_popcount(i) <= k) {
                subsets.push_back(i);
            }
        }

        // dist[mask][stage] is min time with mask at destination and boat at base
        vector<vector<double>> dist(1 << n, vector<double>(m, 1e18));
        priority_queue<pair<double, pair<int, int>>, vector<pair<double, pair<int, int>>>, greater<pair<double, pair<int, int>>>> pq;

        dist[0][0] = 0.0;
        pq.push({0.0, {0, 0}});

        double min_total_time = 1e18;

        while (!pq.empty()) {
            double d = pq.top().first;
            int mask = pq.top().second.first;
            int stage = pq.top().second.second;
            pq.pop();

            if (d > dist[mask][stage]) continue;

            int base_mask = full_mask ^ mask;
            for (int S : subsets) {
                if ((S & base_mask) == S) {
                    int mask_new = mask | S;
                    double t_fwd = max_time[S] * mul[stage];
                    int stage_mid = (stage + (int)floor(t_fwd + 1e-9)) % m;

                    if (mask_new == full_mask) {
                        min_total_time = min(min_total_time, d + t_fwd);
                    } else {
                        // One person must return
                        for (int r = 0; r < n; ++r) {
                            if ((mask_new >> r) & 1) {
                                double t_ret = time[r] * mul[stage_mid];
                                int stage_next = (stage_mid + (int)floor(t_ret + 1e-9)) % m;
                                int mask_final = mask_new ^ (1 << r);
                                if (d + t_fwd + t_ret < dist[mask_final][stage_next]) {
                                    dist[mask_final][stage_next] = d + t_fwd + t_ret;
                                    pq.push({dist[mask_final][stage_next], {mask_final, stage_next}});
                                }
                            }
                        }
                    }
                }
            }
        }

        return (min_total_time > 1e17) ? -1.0 : min_total_time;
    }
};