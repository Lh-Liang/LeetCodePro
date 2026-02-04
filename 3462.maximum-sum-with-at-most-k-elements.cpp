#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        vector<int> selectedElements;
        for (int i = 0; i < grid.size(); ++i) {
            sort(grid[i].begin(), grid[i].end(), greater<int>()); // Sort each row in descending order.
            for (int j = 0; j < min((int)grid[i].size(), limits[i]); ++j) {
                selectedElements.push_back(grid[i][j]); // Collect top elements within limit.
            }
        }
        sort(selectedElements.begin(), selectedElements.end(), greater<int>()); // Sort collected elements globally.
        long long sum = 0;
        for (int i = 0; i < min(k, (int)selectedElements.size()); ++i) {
            sum += selectedElements[i]; // Sum up to K largest elements.
        }
        return sum; // Return maximum sum of selected elements.
    }
};
# @lc code=end