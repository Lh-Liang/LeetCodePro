//
// @lc app=leetcode id=3462 lang=cpp
//
// [3462] Maximum Sum With at Most K Elements
//

// @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        vector<int> candidates;
        
        int n = grid.size();
        for (int i = 0; i < n; i++) {
            vector<int> row = grid[i];
            sort(row.begin(), row.end(), greater<int>());
            for (int j = 0; j < limits[i]; j++) {
                candidates.push_back(row[j]);
            }
        }
        
        sort(candidates.begin(), candidates.end(), greater<int>());
        
        long long sum = 0;
        int count = min(k, (int)candidates.size());
        for (int i = 0; i < count; i++) {
            sum += candidates[i];
        }
        
        return sum;
    }
};
// @lc code=end