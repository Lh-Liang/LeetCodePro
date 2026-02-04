#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = s.length();
        // Step 2: Find first and last occurrence for each character
        vector<int> first(26, n), last(26, -1);
        for (int i = 0; i < n; ++i) {
            int idx = s[i] - 'a';
            first[idx] = min(first[idx], i);
            last[idx] = max(last[idx], i);
        }
        vector<pair<int, int>> intervals;
        // Step 3: Identify all minimal special substrings
        int i = 0;
        while (i < n) {
            // Only start at first occurrence of a character
            if (first[s[i]-'a'] != i) { ++i; continue; }
            int end = last[s[i]-'a'];
            int j = i;
            while (j <= end) {
                end = max(end, last[s[j]-'a']);
                ++j;
            }
            // Exclude the entire string
            if (!(i == 0 && end == n-1)) {
                intervals.push_back({i, end});
            }
            i = end + 1;
        }
        // Step 4: Greedy selection of up to k disjoint intervals
        sort(intervals.begin(), intervals.end(), [](auto& a, auto& b){ return a.second < b.second; });
        int count = 0, last_end = -1;
        for (auto& range : intervals) {
            if (range.first > last_end) {
                ++count;
                last_end = range.second;
                if (count == k) return true;
            }
        }
        return false;
    }
};
# @lc code=end