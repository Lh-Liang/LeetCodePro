# @lc app=leetcode id=3548 lang=cpp
# [3548] Equal Sum Grid Partition II
# @lc code=start
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> rowSums(m), colSums(n);
        int totalSum = 0;
        
        // Calculate row sums and total sum
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rowSums[i] += grid[i][j];
                totalSum += grid[i][j];
            }
        }
        
        // Calculate column sums
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                colSums[j] += grid[i][j];
            }
        }

        // Check horizontal partitions
        int upperSum = 0;
        for (int i = 0; i < m - 1; ++i) {
            upperSum += rowSums[i];
            int lowerSum = totalSum - upperSum;
            if (upperSum == lowerSum) return true;
            // Optionally check for possible discounts here...
        }

        // Check vertical partitions
        int leftSum = 0;
        for (int j = 0; j < n - 1; ++j) {
            leftSum += colSums[j];
            int rightSum = totalSum - leftSum;
            if (leftSum == rightSum) return true;
            // Optionally check for possible discounts here...
        }

        // Implement logic for discounting one cell if necessary...

        return false;
    }
};
# @lc code=end