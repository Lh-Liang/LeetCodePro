#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        vector<int> candidates;
        int n = grid.size();
        for (int i = 0; i < n; ++i) {
            auto row = grid[i];
            sort(row.rbegin(), row.rend());
            int cnt = min((int)row.size(), limits[i]);
            for (int j = 0; j < cnt; ++j) {
                candidates.push_back(row[j]);
            }
        }
        sort(candidates.rbegin(), candidates.rend());
        long long ans = 0;
        for (int i = 0; i < min(k, (int)candidates.size()); ++i) {
            ans += candidates[i];
        }
        return ans;
    }
};
# @lc code=end