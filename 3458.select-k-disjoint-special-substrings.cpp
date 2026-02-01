#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = s.length();
        vector<int> first(26, -1), last(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        vector<pair<int, int>> intervals;
        for (int i = 0; i < 26; ++i) {
            if (first[i] == -1) continue;
            
            int start = first[i];
            int end = last[i];
            bool valid = true;
            
            // Expand the window to include all occurrences of characters within [start, end]
            for (int j = start; j <= end; ++j) {
                int c = s[j] - 'a';
                if (first[c] < start) {
                    valid = false;
                    break;
                }
                end = max(end, last[c]);
            }
            
            // A special substring must not be the entire string
            if (valid && !(start == 0 && end == n - 1)) {
                intervals.push_back({start, end});
            }
        }

        if (intervals.empty()) return k <= 0;

        // Greedy interval scheduling: maximize disjoint intervals by sorting by end time
        sort(intervals.begin(), intervals.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.second != b.second) return a.second < b.second;
            return a.first > b.first;
        });

        int count = 0;
        int last_end = -1;
        for (const auto& interval : intervals) {
            if (interval.first > last_end) {
                count++;
                last_end = interval.second;
            }
        }

        return count >= k;
    }
};
# @lc code=end