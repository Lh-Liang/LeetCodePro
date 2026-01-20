#
# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long total_sum = 0;
        vector<int> freq(100001, 0);
        vector<long long> row_sums(m, 0);
        vector<long long> col_sums(n, 0);

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = grid[i][j];
                total_sum += val;
                freq[val]++;
                row_sums[i] += val;
                col_sums[j] += val;
            }
        }

        // Horizontal cuts
        vector<int> current_freq(100001, 0);
        vector<int> remaining_freq = freq;
        long long s_a = 0;
        for (int i = 0; i < m - 1; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = grid[i][j];
                current_freq[val]++;
                remaining_freq[val]--;
            }
            s_a += row_sums[i];
            long long s_b = total_sum - s_a;

            if (s_a == s_b) return true;

            // Check Section A (rows 0 to i)
            long long x = 2 * s_a - total_sum;
            if (x > 0 && x <= 100000) {
                int h_a = i + 1;
                if (h_a > 1 && n > 1) {
                    if (current_freq[x] > 0) return true;
                } else if (h_a == 1 && n > 1) {
                    if (x == grid[0][0] || x == grid[0][n - 1]) return true;
                } else if (h_a > 1 && n == 1) {
                    if (x == grid[0][0] || x == grid[i][0]) return true;
                } else if (h_a == 1 && n == 1) {
                    if (x == grid[0][0]) return true;
                }
            }

            // Check Section B (rows i+1 to m-1)
            long long y = total_sum - 2 * s_a;
            if (y > 0 && y <= 100000) {
                int h_b = m - 1 - i;
                if (h_b > 1 && n > 1) {
                    if (remaining_freq[y] > 0) return true;
                } else if (h_b == 1 && n > 1) {
                    if (y == grid[i + 1][0] || y == grid[i + 1][n - 1]) return true;
                } else if (h_b > 1 && n == 1) {
                    if (y == grid[i + 1][0] || y == grid[m - 1][0]) return true;
                } else if (h_b == 1 && n == 1) {
                    if (y == grid[i + 1][0]) return true;
                }
            }
        }

        // Vertical cuts
        fill(current_freq.begin(), current_freq.end(), 0);
        remaining_freq = freq;
        s_a = 0;
        for (int j = 0; j < n - 1; ++j) {
            for (int i = 0; i < m; ++i) {
                int val = grid[i][j];
                current_freq[val]++;
                remaining_freq[val]--;
            }
            s_a += col_sums[j];
            long long s_b = total_sum - s_a;

            if (s_a == s_b) return true;

            // Check Section A (cols 0 to j)
            long long x = 2 * s_a - total_sum;
            if (x > 0 && x <= 100000) {
                int w_a = j + 1;
                if (m > 1 && w_a > 1) {
                    if (current_freq[x] > 0) return true;
                } else if (m == 1 && w_a > 1) {
                    if (x == grid[0][0] || x == grid[0][j]) return true;
                } else if (m > 1 && w_a == 1) {
                    if (x == grid[0][0] || x == grid[m - 1][0]) return true;
                } else if (m == 1 && w_a == 1) {
                    if (x == grid[0][0]) return true;
                }
            }

            // Check Section B (cols j+1 to n-1)
            long long y = total_sum - 2 * s_a;
            if (y > 0 && y <= 100000) {
                int w_b = n - 1 - j;
                if (m > 1 && w_b > 1) {
                    if (remaining_freq[y] > 0) return true;
                } else if (m == 1 && w_b > 1) {
                    if (y == grid[0][j + 1] || y == grid[0][n - 1]) return true;
                } else if (m > 1 && w_b == 1) {
                    if (y == grid[0][j + 1] || y == grid[m - 1][j + 1]) return true;
                } else if (m == 1 && w_b == 1) {
                    if (y == grid[0][j + 1]) return true;
                }
            }
        }

        return false;
    }
};
# @lc code=end