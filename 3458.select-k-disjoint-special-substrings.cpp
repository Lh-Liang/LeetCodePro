#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3458 lang=cpp
 *
 * [3458] Select K Disjoint Special Substrings
 */

// @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = (int)s.size();

        vector<int> first(26, n), last(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            first[c] = min(first[c], i);
            last[c] = max(last[c], i);
        }

        auto buildInterval = [&](int l) -> pair<int,int> {
            int r = last[s[l] - 'a'];
            for (int i = l; i <= r; ++i) {
                int c = s[i] - 'a';
                if (first[c] < l) return {-1, -1}; // invalid
                r = max(r, last[c]);
            }
            return {l, r};
        };

        vector<pair<int,int>> intervals;
        intervals.reserve(26);
        for (int c = 0; c < 26; ++c) {
            if (last[c] == -1) continue; // not present
            int l = first[c];
            auto seg = buildInterval(l);
            if (seg.first == -1) continue;
            // cannot be the entire string
            if (seg.first == 0 && seg.second == n - 1) continue;
            intervals.push_back(seg);
        }

        sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            if (a.second != b.second) return a.second < b.second;
            return a.first < b.first;
        });

        int cnt = 0;
        int prevEnd = -1;
        for (auto [l, r] : intervals) {
            if (l > prevEnd) {
                ++cnt;
                prevEnd = r;
                if (cnt >= k) return true;
            }
        }
        return cnt >= k;
    }
};
// @lc code=end
