#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        int n = grid.size();
        vector<int> candidates;
        
        // Step 1: Local Optimization - For each row, take the largest 'limits[i]' elements.
        for (int i = 0; i < n; ++i) {
            // Sort row in descending order to easily pick the largest elements
            sort(grid[i].begin(), grid[i].end(), greater<int>());
            
            // Take up to limits[i] elements from the current row
            int take = min((int)grid[i].size(), limits[i]);
            for (int j = 0; j < take; ++j) {
                candidates.push_back(grid[i][j]);
            }
        }
        
        // Step 2: Global Aggregation - From the pool of locally optimal elements, pick the top k.
        sort(candidates.begin(), candidates.end(), greater<int>());
        
        long long totalSum = 0;
        // Ensure we don't exceed the number of available candidates if k is larger
        int finalTake = min((int)candidates.size(), k);
        for (int i = 0; i < finalTake; ++i) {
            totalSum += candidates[i];
        }
        
        return totalSum;
    }
};
# @lc code=end