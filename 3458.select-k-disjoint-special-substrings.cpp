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
        vector<int> L(26, -1), R(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            if (L[c] == -1) L[c] = i;
            R[c] = i;
        }

        vector<pair<int, int>> intervals;
        for (int i = 0; i < 26; ++i) {
            if (L[i] == -1) continue;
            int start = L[i];
            int end = R[i];
            bool valid = true;
            
            // Expand the interval to include all occurrences of characters inside it
            for (int j = start; j <= end; ++j) {
                int char_idx = s[j] - 'a';
                if (L[char_idx] < start) {
                    valid = false; // Cannot form a valid range starting from L[i]
                    break;
                }
                if (R[char_idx] > end) {
                    end = R[char_idx];
                }
            }
            
            // Special substring cannot be the entire string
            if (valid && (end - start + 1) < n) {
                intervals.push_back({start, end});
            }
        }

        if (intervals.empty()) return k <= 0;

        // Greedy Interval Scheduling: Sort by end time
        sort(intervals.begin(), intervals.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
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