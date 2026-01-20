#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();
        long long total_sum = 0;
        int sink_index = -1;

        // Identify if there is a negative balance and check total sum
        for (int i = 0; i < n; ++i) {
            total_sum += balance[i];
            if (balance[i] < 0) {
                sink_index = i;
            }
        }

        // If total sum is negative, it's impossible to balance
        if (total_sum < 0) {
            return -1;
        }

        // If no negative balance exists, 0 moves are needed
        if (sink_index == -1) {
            return 0;
        }

        long long deficit = -(long long)balance[sink_index];
        // Collect surplus available at each distance from the sink
        // Max distance in a circular array of size n is n/2
        vector<long long> surplus_at_dist(n / 2 + 1, 0);

        for (int i = 0; i < n; ++i) {
            if (i == sink_index) continue;
            if (balance[i] > 0) {
                int d = abs(i - sink_index);
                d = min(d, n - d);
                surplus_at_dist[d] += balance[i];
            }
        }

        long long total_moves = 0;
        // Greedily take surplus from the nearest neighbors first
        for (int d = 1; d <= n / 2; ++d) {
            if (deficit <= 0) break;
            long long take = min(deficit, surplus_at_dist[d]);
            total_moves += take * d;
            deficit -= take;
        }

        return total_moves;
    }
};
# @lc code=end