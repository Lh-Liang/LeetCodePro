#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        vector<int> selected;
        for (int i = 0; i < grid.size(); ++i) {
            sort(grid[i].begin(), grid[i].end(), greater<int>());
            for (int j = 0; j < min(limits[i], static_cast<int>(grid[i].size())); ++j) {
                selected.push_back(grid[i][j]);
            }
        }
        sort(selected.begin(), selected.end(), greater<int>());
        long long max_sum = 0;
        for (int i = 0; i < min(k, static_cast<int>(selected.size())); ++i) {
            max_sum += selected[i];
        }
        return max_sum;
    }
};
# @lc code=end