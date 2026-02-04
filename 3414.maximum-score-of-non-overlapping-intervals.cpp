#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#
# @lc code=start
class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        // Sort intervals based on end time (ri) and start time (li) for stability in lexicographical order
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1] || (a[1] == b[1] && a[0] < b[0]);
        });
        
        int n = intervals.size();
        vector<vector<int>> dp(n + 1, vector<int>(5, 0)); // dp[i][j]: max score using first i intervals with j selections
        vector<vector<vector<int>>> choices(n + 1, vector<vector<int>>(5)); // track chosen indices for reconstruction
        
        for (int i = 1; i <= n; ++i) {
            int li = intervals[i-1][0], ri = intervals[i-1][1], w = intervals[i-1][2];
            for (int j = 0; j <= 4; ++j) {
                // Not taking this interval at all (carry over previous best)
                dp[i][j] = dp[i-1][j];
                choices[i][j] = choices[i-1][j];
                
                if (j > 0) { // Consider taking this interval if j > 0 selections allowed & it doesn't overlap with any in 'choices' set. & its weight benefits us more. & prev_end <= current_start condition met. & update choice set accordingly based on lexicographical order as well. & if(dp[i][j] < dp[k+1][j-1]+w){dp[i][j]=dp[k+1][j-1]+w;}prev_end=k>=0?k.end:-infinity;for(k=i-2;k>=0&&intervals[k].end>li;k--);choices[i][j]=choices[k+1][j-1];choices[i][j].push_back(i-1);}}}return choices[n][4];}}; # @lc code=end