#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
#include <vector>
#include <numeric>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();
        long long total_sum = 0;
        int neg_idx = -1;

        for (int i = 0; i < n; ++i) {
            total_sum += balance[i];
            if (balance[i] < 0) {
                neg_idx = i;
            }
        }

        if (total_sum < 0) return -1;
        if (neg_idx == -1) return 0;

        long long deficit = -static_cast<long long>(balance[neg_idx]);
        struct Source {
            int amount;
            int distance;
        };
        vector<Source> sources;

        for (int i = 0; i < n; ++i) {
            if (balance[i] > 0) {
                int dist = abs(i - neg_idx);
                dist = min(dist, n - dist);
                sources.push_back({balance[i], dist});
            }
        }

        sort(sources.begin(), sources.end(), [](const Source& a, const Source& b) {
            return a.distance < b.distance;
        });

        long long total_moves = 0;
        for (const auto& src : sources) {
            if (deficit <= 0) break;
            long long take = min((long long)src.amount, deficit);
            total_moves += take * src.distance;
            deficit -= take;
        }

        return total_moves;
    }
};
# @lc code=end