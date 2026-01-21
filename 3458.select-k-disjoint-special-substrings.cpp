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
            last[c] = i;
        }

        vector<pair<int,int>> intervals;
        intervals.reserve(26);

        for (int c = 0; c < 26; ++c) {
            if (first[c] == n) continue; // not present
            int l = first[c];
            int r = last[c];
            bool ok = true;
            for (int j = l; j <= r; ++j) {
                int d = s[j] - 'a';
                if (first[d] < l) { // appears outside on the left
                    ok = false;
                    break;
                }
                r = max(r, last[d]);
            }
            if (ok) intervals.push_back({l, r});
        }

        sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            if (a.second != b.second) return a.second < b.second;
            return a.first > b.first; // tie-break (not strictly necessary)
        });

        int cnt = 0;
        int end = -1;
        for (auto [l, r] : intervals) {
            if (l <= end) continue;
            if (l == 0 && r == n - 1) continue; // cannot pick the entire string
            ++cnt;
            end = r;
            if (cnt >= k) return true;
        }
        return false;
    }
};
// @lc code=end
