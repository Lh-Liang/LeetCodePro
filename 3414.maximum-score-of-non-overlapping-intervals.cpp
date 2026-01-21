#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if (n == 0) return {};
        struct Interval {
            int l, r, w, idx;
        };
        vector<Interval> ints(n);
        for (int i = 0; i < n; ++i) {
            ints[i].l = intervals[i][0];
            ints[i].r = intervals[i][1];
            ints[i].w = intervals[i][2];
            ints[i].idx = i;
        }
        sort(ints.begin(), ints.end(), [](const Interval& a, const Interval& b) {
            if (a.r != b.r) return a.r < b.r;
            return a.idx < b.idx;
        });
        vector<int> pre(n, -1);
        for (int i = 0; i < n; ++i) {
            int target = ints[i].l;
            int low = 0, high = i - 1;
            int ans = -1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (ints[mid].r < target) {
                    ans = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            pre[i] = ans;
        }
        using ll = long long;
        vector<vector<ll>> dp(5, vector<ll>(n, LLONG_MIN / 2));
        vector<vector<vector<int>>> best_path(5, vector<vector<int>>(n));
        for (int i = 0; i < n; ++i) {
            dp[1][i] = ints[i].w;
            best_path[1][i] = {ints[i].idx};
        }
        for (int jj = 2; jj <= 4; ++jj) {
            vector<ll> prefix_score(n);
            vector<vector<int>> prefix_best(n);
            prefix_score[0] = dp[jj - 1][0];
            prefix_best[0] = best_path[jj - 1][0];
            for (int m = 1; m < n; ++m) {
                prefix_score[m] = prefix_score[m - 1];
                prefix_best[m] = prefix_best[m - 1];
                if (dp[jj - 1][m] > prefix_score[m]) {
                    prefix_score[m] = dp[jj - 1][m];
                    prefix_best[m] = best_path[jj - 1][m];
                } else if (dp[jj - 1][m] == prefix_score[m]) {
                    vector<int> cand = best_path[jj - 1][m];
                    if (cand < prefix_best[m]) {
                        prefix_best[m] = cand;
                    }
                }
            }
            for (int i = 0; i < n; ++i) {
                int p = pre[i];
                if (p >= 0) {
                    ll prev_s = prefix_score[p];
                    vector<int> prev_list = prefix_best[p];
                    prev_list.push_back(ints[i].idx);
                    sort(prev_list.begin(), prev_list.end());
                    dp[jj][i] = prev_s + (ll)ints[i].w;
                    best_path[jj][i] = move(prev_list);
                }
            }
        }
        ll max_score = 0;
        vector<int> result;
        for (int j = 1; j <= 4; ++j) {
            for (int i = 0; i < n; ++i) {
                if (dp[j][i] > max_score) {
                    max_score = dp[j][i];
                    result = best_path[j][i];
                } else if (dp[j][i] == max_score) {
                    if (best_path[j][i] < result) {
                        result = best_path[j][i];
                    }
                }
            }
        }
        return result;
    }
};
# @lc code=end