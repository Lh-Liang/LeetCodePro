#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

struct Interval {
    int l, r, w, id;
};

class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<Interval> ivs(n);
        for (int i = 0; i < n; ++i) {
            ivs[i] = {intervals[i][0], intervals[i][1], intervals[i][2], i};
        }

        // Sort by start time
        sort(ivs.begin(), ivs.end(), [](const Interval& a, const Interval& b) {
            return a.l < b.l;
        });

        // dp[k][i] stores {max_weight, sorted_indices}
        // Using k from 1 to 4 and i from n down to 0
        using State = pair<long long, vector<int>>;
        auto compare = [](const State& a, const State& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second; // Lexicographically smaller vector is "greater" in our max search
        };

        vector<vector<State>> dp(5, vector<State>(n + 1, {0, {}}));

        // Precompute next interval index using binary search
        vector<int> next_idx(n);
        for (int i = 0; i < n; ++i) {
            int low = i + 1, high = n;
            while (low < high) {
                int mid = low + (high - low) / 2;
                if (ivs[mid].l > ivs[i].r) high = mid;
                else low = mid + 1;
            }
            next_idx[i] = low;
        }

        for (int k = 1; k <= 4; ++k) {
            for (int i = n - 1; i >= 0; --i) {
                // Option 1: Skip current interval
                dp[k][i] = dp[k][i+1];

                // Option 2: Take current interval
                long long current_w = ivs[i].w + dp[k-1][next_idx[i]].first;
                vector<int> current_indices = {ivs[i].id};
                for (int idx : dp[k-1][next_idx[i]].second) current_indices.push_back(idx);
                sort(current_indices.begin(), current_indices.end());

                State take_state = {current_w, current_indices};
                if (compare(dp[k][i], take_state)) {
                    dp[k][i] = take_state;
                }
            }
        }

        return dp[4][0].second;
    }
};
# @lc code=end