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
        // Step 1: Sort segments by starting position
        vector<tuple<ll,ll,ll>> segs;
        for (const auto& c : coins) {
            segs.emplace_back((ll)c[0], (ll)c[1], (ll)c[2]);
        }
        sort(segs.begin(), segs.end());
        // Step 2: Build intervals and coin values
        vector<pair<ll,ll>> intervals; // {start, coin value}
        ll prev = 1;
        for (auto [l, r, c] : segs) {
            if (prev < l) intervals.push_back({prev, 0}); // gap
            intervals.push_back({l, c});
            prev = r + 1;
        }
        // No need to add infinite tail, as window will not go to infinity
        // Step 3: Sliding window over intervals
        int n = intervals.size();
        ll ans = 0, sum = 0;
        int j = 0;
        ll window_left = intervals[0].first;
        ll window_right = window_left + k - 1;
        ll right = window_left;
        // initialize window
        for (j = 0; j < n && intervals[j].first <= window_right; ++j) {
            ll seg_start = intervals[j].first;
            ll seg_end = (j+1<n ? intervals[j+1].first : window_right+1) - 1;
            ll seg_l = max(seg_start, window_left);
            ll seg_r = min(seg_end, window_right);
            if (seg_l <= seg_r) sum += (seg_r - seg_l + 1) * intervals[j].second;
        }
        ans = sum;
        // Slide window
        for (ll L = window_left + 1; ; ++L) {
            ll R = L + k - 1;
            if (R < intervals[0].first) continue;
            if (R >= intervals.back().first + (j < n ? 0 : 1e9)) break; // window out of all segments
            // Remove leftmost
            int i = lower_bound(intervals.begin(), intervals.end(), make_pair(L-1, LLONG_MIN)) - intervals.begin();
            if (i && intervals[i-1].first <= L-1 && (i == n || L-1 < intervals[i].first)) {
                sum -= intervals[i-1].second;
            }
            // Add rightmost
            int rj = lower_bound(intervals.begin(), intervals.end(), make_pair(R, LLONG_MIN)) - intervals.begin();
            if (rj && intervals[rj-1].first <= R && (rj == n || R < intervals[rj].first)) {
                sum += intervals[rj-1].second;
            }
            ans = max(ans, sum);
        }
        return ans;
    }
};
# @lc code=end