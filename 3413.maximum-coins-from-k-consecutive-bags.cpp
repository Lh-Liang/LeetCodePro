#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        using ll = long long;
        vector<array<ll, 3>> intervals;
        for (const auto& c : coins) {
            intervals.push_back({(ll)c[0], (ll)c[1], (ll)c[2]});
        }
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        // Build a list of all interval boundaries
        vector<ll> points;
        for (const auto& seg : intervals) {
            points.push_back(seg[0]);
            points.push_back(seg[1] + 1);
        }
        sort(points.begin(), points.end());
        points.erase(unique(points.begin(), points.end()), points.end());
        // For each interval between two points, compute its coin value
        vector<ll> coin_in_gap(points.size() - 1, 0);
        int j = 0;
        for (int i = 0; i < points.size() - 1; ++i) {
            ll l = points[i], r = points[i + 1] - 1;
            while (j < n && intervals[j][1] < l) ++j;
            if (j < n && intervals[j][0] <= l && r <= intervals[j][1]) {
                coin_in_gap[i] = intervals[j][2];
            } else {
                coin_in_gap[i] = 0;
            }
        }
        // Sliding window over the compressed intervals
        int left = 0;
        ll curr_sum = 0, max_sum = 0, curr_len = 0;
        for (int right = 0; right < coin_in_gap.size(); ++right) {
            ll seg_len = points[right + 1] - points[right];
            curr_sum += coin_in_gap[right] * seg_len;
            curr_len += seg_len;
            while (curr_len > k) { // shrink from left
                ll remove_len = min(curr_len - k, points[left + 1] - points[left]);
                curr_sum -= coin_in_gap[left] * remove_len;
                curr_len -= remove_len;
                if (remove_len == points[left + 1] - points[left]) {
                    ++left;
                } else {
                    break;
                }
            }
            if (curr_len == k) {
                max_sum = max(max_sum, curr_sum);
            }
        }
        return max_sum;
    }
};
# @lc code=end