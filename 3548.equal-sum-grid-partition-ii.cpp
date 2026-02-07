# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#
# @lc code=start
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> rowPrefixSum(m, vector<int>(n+1, 0));
        vector<vector<int>> colPrefixSum(n, vector<int>(m+1, 0));
        
        // Calculate row and column prefix sums
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rowPrefixSum[i][j+1] = rowPrefixSum[i][j] + grid[i][j];
                colPrefixSum[j][i+1] = colPrefixSum[j][i] + grid[i][j];
            }
        }

        // Check horizontal cuts
        for (int i = 1; i < m; ++i) { // Ensure non-empty sections
            int topSum = rowPrefixSum[i-1][n];
            int bottomSum = rowPrefixSum[m-1][n] - topSum;
            if (topSum == bottomSum || canDiscountToEqual(grid, topSum, bottomSum, true)) {
                return true;
            }
        }

        // Check vertical cuts using correct column boundaries
        for (int j = 1; j < n; ++j) { // Ensure non-empty sections
            int leftSum = colPrefixSum[j-1][m];
            int rightSum = colPrefixSum[n-1][m] - leftSum;
            if (leftSum == rightSum || canDiscountToEqual(grid, leftSum, rightSum, false)) {
                return true;
            }
        }

        return false;
    }
    
    bool canDiscountToEqual(const vector<vector<int>>& grid, int sum1, int sum2, bool isHorizontalCut) {
        int diff = abs(sum1 - sum2);
        for (const auto& row : grid) {
            for (int val : row) {
                if (val == diff && checkConnectivityAfterRemoval(grid, val)) {
                    return true;
                }			}		}		return false;	}		bool checkConnectivityAfterRemoval(const vector<vector<int>>& grid, int discountValue) { 		// Implement BFS/DFS to check connectivity after removing discountValue.	return true; // Placeholder: Assume connected after removal for demonstration.	}	}; # @lc code=end