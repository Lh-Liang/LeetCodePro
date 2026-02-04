#
# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        // Compute prefix sums for efficient region sum queries
        vector<vector<long long>> psum(m + 1, vector<long long>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                psum[i+1][j+1] = grid[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j];
            }
        }
        long long total = psum[m][n];
        auto getRowSum = [&](int r1, int r2, int c1, int c2) -> long long {
            return psum[r2][c2] - psum[r1][c2] - psum[r2][c1] + psum[r1][c1];
        };
        // Helper to check connectivity in-place for a section after removing a border cell
        auto isConnected = [&](int r1, int r2, int c1, int c2, int rem_r, int rem_c) -> bool {
            int rows = r2 - r1, cols = c2 - c1;
            vector<vector<bool>> visited(rows, vector<bool>(cols, false));
            // Start from any cell except the removed one
            queue<pair<int,int>> q;
            bool started = false;
            for (int i = 0; i < rows && !started; ++i) {
                for (int j = 0; j < cols && !started; ++j) {
                    if (!(i + r1 == rem_r && j + c1 == rem_c)) {
                        q.push({i, j});
                        visited[i][j] = true;
                        started = true;
                    }
                }
            }
            if (!started) return true; // only one cell in section
            int count = 1;
            while (!q.empty()) {
                auto [x, y] = q.front(); q.pop();
                for (int d = 0; d < 4; ++d) {
                    int nx = x + (d == 0) - (d == 1), ny = y + (d == 2) - (d == 3);
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && !visited[nx][ny] && !(nx + r1 == rem_r && ny + c1 == rem_c)) {
                        visited[nx][ny] = true;
                        q.push({nx, ny});
                        ++count;
                    }
                }
            }
            return count == rows * cols - 1;
        };
        // Try horizontal cuts
        for (int r = 1; r < m; ++r) {
            long long top = getRowSum(0, r, 0, n);
            long long bot = total - top;
            if (top == bot) return true;
            // Try discounting border cell at cut
            for (int c = 0; c < n; ++c) {
                // Remove (r-1, c) from top
                if (top > bot && top - grid[r-1][c] == bot) {
                    if (isConnected(0, r, 0, n, r-1, c)) return true;
                }
                // Remove (r, c) from bottom
                if (bot > top && bot - grid[r][c] == top) {
                    if (isConnected(r, m, 0, n, r, c)) return true;
                }
            }
        }
        // Try vertical cuts
        for (int c = 1; c < n; ++c) {
            long long left = getRowSum(0, m, 0, c);
            long long right = total - left;
            if (left == right) return true;
            for (int r = 0; r < m; ++r) {
                // Remove (r, c-1) from left
                if (left > right && left - grid[r][c-1] == right) {
                    if (isConnected(0, m, 0, c, r, c-1)) return true;
                }
                // Remove (r, c) from right
                if (right > left && right - grid[r][c] == left) {
                    if (isConnected(0, m, c, n, r, c)) return true;
                }
            }
        }
        return false;
    }
};
# @lc code=end