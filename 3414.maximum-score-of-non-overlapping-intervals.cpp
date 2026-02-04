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
        // Sort intervals by end time; if equal, by start time for stability
        sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) { 
            return (a[1] < b[1]) || (a[1] == b[1] && a[0] < b[0]);
        });
        // Dynamic programming table storing scores and index vectors
        vector<pair<int, vector<int>>> dp; 
        for (int i = 0; i < intervals.size(); ++i) {
            // Binary search for the last non-overlapping interval
            int l = 0, r = dp.size();
            while (l < r) { 
                int mid = (l + r) / 2;
                if (dp[mid].second.empty() || intervals[dp[mid].second.back()][1] < intervals[i][0]) l = mid + 1;
                else r = mid;
            }
            int current_score = (r > 0 ? dp[r-1].first : 0) + intervals[i][2];
            vector<int> new_entry;
            if (r > 0) new_entry.insert(new_entry.end(), dp[r-1].second.begin(), dp[r-1].second.end());
            new_entry.push_back(i);
            if (new_entry.size() > 4) continue; // Skip if more than four indices
            // Compare with last entry in dp table for potential update
            if (dp.empty() || dp.back().first < current_score || \
               (dp.back().first == current_score && lexicographical_compare(new_entry.begin(), new_entry.end(), dp.back().second.begin(), dp.back().second.end()))) {
                if (!dp.empty() && dp.back().first == current_score) dp.pop_back();
                dp.push_back({current_score, new_entry});
            }
        }
        return dp.empty() ? vector<int>() : dp.back().second;
    }
};
# @lc code=end