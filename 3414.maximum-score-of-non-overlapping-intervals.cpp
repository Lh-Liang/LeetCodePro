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

struct State {
    long long weight = 0;
    vector<int> ids;

    bool betterThan(const State& other) const {
        if (weight != other.weight) return weight > other.weight;
        return ids < other.ids;
    }
};

class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<Interval> ivs(n);
        for (int i = 0; i < n; ++i) {
            ivs[i] = {intervals[i][0], intervals[i][1], intervals[i][2], i};
        }

        sort(ivs.begin(), ivs.end(), [](const Interval& a, const Interval& b) {
            return a.r < b.r;
        });

        vector<int> ends;
        for (auto& iv : ivs) ends.push_back(iv.r);

        // dp[count][i] stores the best State using 'count' intervals from first 'i' sorted intervals
        vector<vector<State>> dp(5, vector<State>(n + 1));

        for (int i = 1; i <= n; ++i) {
            int cur_l = ivs[i - 1].l;
            int cur_w = ivs[i - 1].w;
            int cur_id = ivs[i - 1].id;

            // Find predecessor: last interval j such that ivs[j-1].r < cur_l
            int prev_idx = lower_bound(ends.begin(), ends.end(), cur_l) - ends.begin();

            for (int k = 1; k <= 4; ++k) {
                // Case 1: Skip current interval
                dp[k][i] = dp[k][i - 1];

                // Case 2: Use current interval
                State current;
                current.weight = (long long)cur_w + dp[k - 1][prev_idx].weight;
                current.ids = dp[k - 1][prev_idx].ids;
                current.ids.push_back(cur_id);
                sort(current.ids.begin(), current.ids.end());

                if (current.betterThan(dp[k][i])) {
                    dp[k][i] = current;
                }
            }
        }

        State best;
        for (int k = 1; k <= 4; ++k) {
            if (dp[k][n].betterThan(best)) {
                best = dp[k][n];
            }
        }

        return best.ids;
    }
};
# @lc code=end