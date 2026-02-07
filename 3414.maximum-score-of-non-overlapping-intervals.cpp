#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        // Sort intervals based on their end time.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        // Dynamic Programming table to store max weight up to each interval.
        vector<pair<int, vector<int>>> dp(intervals.size(), {0, {}});
        
        for (int i = 0; i < intervals.size(); ++i) {
            int current_weight = intervals[i][2];
            int l = 0, r = i - 1;
            
            // Binary search to find non-overlapping previous interval.
            while (l <= r) {
                int mid = l + (r - l) / 2;
                if (intervals[mid][1] < intervals[i][0]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            
            if (r >= 0) { // Add weight if found non-overlapping interval. 
                current_weight += dp[r].first; 
            } 
            
            // Compare and decide whether to include this interval. 
            if (i > 0 && dp[i-1].first > current_weight) { 
                dp[i] = dp[i-1]; 
            } else { 
                dp[i].first = current_weight; 
                if (r >= 0) dp[i].second = dp[r].second; 
                dp[i].second.push_back(i); 
            } 

        } 
      
      // Return indices of selected intervals with max score.
      return dp.back().second.size() > 4 ? vector<int>(dp.back().second.begin(), dp.back().second.begin() + 4) : dp.back().second; 
    }
};
# @lc code=end