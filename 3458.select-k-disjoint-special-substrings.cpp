#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        int n = s.size();
        vector<int> first(26, n), last(26, -1);
        // Step 1: Record first and last occurrence of each character
        for (int i = 0; i < n; ++i) {
            int idx = s[i] - 'a';
            if (first[idx] == n) first[idx] = i;
            last[idx] = i;
        }
        // Step 2: Generate candidate intervals
        vector<pair<int, int>> intervals;
        for (int ch = 0; ch < 26; ++ch) {
            if (first[ch] < last[ch]) { // must not be the entire string
                int l = first[ch], r = last[ch];
                bool valid = true;
                // Step 3: Check all chars inside interval
                for (int i = l; i <= r && valid; ++i) {
                    int ci = s[i] - 'a';
                    if (first[ci] < l || last[ci] > r) valid = false;
                }
                if (valid) intervals.push_back({l, r});
            }
        }
        // Step 4: Greedy: sort by end, select disjoint
        sort(intervals.begin(), intervals.end(), [](auto&a, auto&b){ return a.second < b.second; });
        int cnt = 0, end = -1;
        for (auto &[l, r] : intervals) {
            if (l > end) {
                ++cnt;
                end = r;
                if (cnt == k) return true;
            }
        }
        // Step 5: Check if we have k substrings
        return k == 0 || cnt >= k;
    }
};
# @lc code=end