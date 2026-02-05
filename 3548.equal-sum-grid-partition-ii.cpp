{
"reasoning": "Step 1: Compute prefix sums for rows and columns to allow efficient section sum queries for each cut. Step 2: For each possible horizontal and vertical cut, compute sums for both sections. If sums equal, return true. Step 3: If not, for each border cell on the cut, check if discounting it equalizes sums and maintains connectivity (discount only edge cells, not interior or bridge cells). Step 4: If no valid cut or discount is found, return false.",
"result": "#
# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        long long total = 0;
        vector<long long> row_sum(m, 0), col_sum(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                total += grid[i][j];
                row_sum[i] += grid[i][j];
                col_sum[j] += grid[i][j];
            }
        }
        vector<long long> prefix_row(m + 1, 0), prefix_col(n + 1, 0);
        for (int i = 0; i < m; ++i) prefix_row[i + 1] = prefix_row[i] + row_sum[i];
        for (int j = 0; j < n; ++j) prefix_col[j + 1] = prefix_col[j] + col_sum[j];
        // Horizontal cuts
        for (int cut = 1; cut < m; ++cut) {
            long long top = prefix_row[cut], bot = total - top;
            if (top == bot) return true;
            long long diff = abs(top - bot);
            // Try discounting a cell on the border (cut row)
            if (top > bot) {
                // Discount from top section, only last row considered
                for (int j = 0; j < n; ++j) {
                    if (top - grid[cut-1][j] == bot) return true;
                }
                // Discount from bottom section, only first row
                for (int j = 0; j < n; ++j) {
                    if (top == bot - grid[cut][j]) return true;
                }
            } else {
                // Discount from bottom section
                for (int j = 0; j < n; ++j) {
                    if (top == bot - grid[cut][j]) return true;
                }
                // Discount from top section
                for (int j = 0; j < n; ++j) {
                    if (top - grid[cut-1][j] == bot) return true;
                }
            }
        }
        // Vertical cuts
        for (int cut = 1; cut < n; ++cut) {
            long long left = prefix_col[cut], right = total - left;
            if (left == right) return true;
            long long diff = abs(left - right);
            if (left > right) {
                // Discount from left section (last col)
                for (int i = 0; i < m; ++i) {
                    if (left - grid[i][cut-1] == right) return true;
                }
                // Discount from right section (first col)
                for (int i = 0; i < m; ++i) {
                    if (left == right - grid[i][cut]) return true;
                }
            } else {
                // Discount from right section
                for (int i = 0; i < m; ++i) {
                    if (left == right - grid[i][cut]) return true;
                }
                // Discount from left section
                for (int i = 0; i < m; ++i) {
                    if (left - grid[i][cut-1] == right) return true;
                }
            }
        }
        return false;
    }
};
# @lc code=end