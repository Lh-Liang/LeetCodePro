#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<tuple<int,int,int,int>> tmp;
        for (int i = 0; i < n; ++i) {
            tmp.emplace_back(intervals[i][1], intervals[i][0], intervals[i][2], i);
        }
        sort(tmp.begin(), tmp.end());
        // dp[i][k]: pair of (score, indices) for first i intervals, using k intervals
        vector<vector<pair<long long, vector<int>>>> dp(n+1, vector<pair<long long, vector<int>>>(5, {0, {}}));
        vector<int> ends(n);
        for (int i = 0; i < n; ++i) ends[i] = get<0>(tmp[i]);
        for (int i = 1; i <= n; ++i) {
            auto [end, start, weight, idx] = tmp[i-1];
            // find prev that does not overlap
            int l = 0, r = i-1, pre = 0;
            while (l < r) {
                int m = (l + r) / 2;
                if (ends[m] < start) l = m+1;
                else r = m;
            }
            pre = (ends[0] < start) ? l+1 : 0;
            for (int k = 1; k <= 4; ++k) {
                // not take
                if (dp[i-1][k].first > dp[i][k].first || 
                    (dp[i-1][k].first == dp[i][k].first && dp[i-1][k].second < dp[i][k].second)) {
                    dp[i][k] = dp[i-1][k];
                }
                // take
                if (dp[pre][k-1].first + weight > dp[i][k].first) {
                    dp[i][k].first = dp[pre][k-1].first + weight;
                    dp[i][k].second = dp[pre][k-1].second;
                    dp[i][k].second.push_back(idx);
                } else if (dp[pre][k-1].first + weight == dp[i][k].first) {
                    auto cand = dp[pre][k-1].second;
                    cand.push_back(idx);
                    if (cand < dp[i][k].second) {
                        dp[i][k].second = cand;
                    }
                }
            }
        }
        long long best = 0;
        vector<int> ans;
        for (int k = 1; k <= 4; ++k) {
            if (dp[n][k].first > best) {
                best = dp[n][k].first;
                ans = dp[n][k].second;
            } else if (dp[n][k].first == best && (ans.empty() || dp[n][k].second < ans)) {
                ans = dp[n][k].second;
            }
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};
# @lc code=end