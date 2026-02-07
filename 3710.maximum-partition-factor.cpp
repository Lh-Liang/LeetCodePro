#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        // Sorting points based on x+y and x-y helps to manage quadrant separation
        vector<int> x_plus_y, x_minus_y;
        for (const auto& p : points) {
            x_plus_y.push_back(p[0] + p[1]);
            x_minus_y.push_back(p[0] - p[1]);
        }
        sort(x_plus_y.begin(), x_plus_y.end());
        sort(x_minus_y.begin(), x_minus_y.end());
        
        // Compute maximum partition factor by evaluating splits at mid-points of sorted arrays
        int n = points.size();
        int result = 0;
        result = max(result, abs(x_plus_y[n-1] - x_plus_y[0]));  // Max difference in sorted sums 
        result = max(result, abs(x_minus_y[n-1] - x_minus_y[0])); // Max difference in sorted differences 
        return result; // Return max partition factor achieved from evaluated splits 
    }
};
# @lc code=end