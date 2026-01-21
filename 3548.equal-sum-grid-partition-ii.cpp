#
# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return false;
        int n = grid[0].size();
        long long total = 0;
        vector<long long> row_sum(m, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                total += grid[i][j];
                row_sum[i] += grid[i][j];
            }
        }
        vector<long long> pref_row(m + 1, 0);
        for (int i = 1; i <= m; i++) {
            pref_row[i] = pref_row[i - 1] + row_sum[i - 1];
        }
        vector<long long> col_sum(n, 0);
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                col_sum[j] += grid[i][j];
            }
        }
        vector<long long> pref_col(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            pref_col[j] = pref_col[j - 1] + col_sum[j - 1];
        }
        const int MAXV = 100001;
        vector<vector<int>> rows_with(MAXV);
        vector<vector<int>> cols_with(MAXV);
        for (int i = 0; i < m; i++) {
            unordered_set<int> vals;
            for (int j = 0; j < n; j++) {
                int v = grid[i][j];
                if (v < MAXV) vals.insert(v);
            }
            for (int v : vals) {
                if (v < MAXV) rows_with[v].push_back(i);
            }
        }
        for (int j = 0; j < n; j++) {
            unordered_set<int> vals;
            for (int i = 0; i < m; i++) {
                int v = grid[i][j];
                if (v < MAXV) vals.insert(v);
            }
            for (int v : vals) {
                if (v < MAXV) cols_with[v].push_back(j);
            }
        }
        auto has_row = [&](int d, int ra, int rb) -> bool {
            if (d >= MAXV || d < 0) return false;
            auto& lis = rows_with[d];
            auto it = lower_bound(lis.begin(), lis.end(), ra);
            return it != lis.end() && *it <= rb;
        };
        auto has_col = [&](int d, int ca, int cb) -> bool {
            if (d >= MAXV || d < 0) return false;
            auto& lis = cols_with[d];
            auto it = lower_bound(lis.begin(), lis.end(), ca);
            return it != lis.end() && *it <= cb;
        };
        auto can_rm = [&](int r1, int r2, int c1, int c2, long long d) -> bool {
            if (d < 1 || d >= MAXV) return false;
            int dd = (int)d;
            int hh = r2 - r1 + 1;
            int ww = c2 - c1 + 1;
            if (hh == 1 && ww == 1) return false;
            if (hh >= 2 && ww >= 2) {
                if (c1 == 0 && c2 == n - 1) {
                    return has_row(dd, r1, r2);
                } else if (r1 == 0 && r2 == m - 1) {
                    return has_col(dd, c1, c2);
                }
                return false;
            } else if (hh == 1) {
                return grid[r1][c1] == dd || grid[r1][c2] == dd;
            } else if (ww == 1) {
                return grid[r1][c1] == dd || grid[r2][c1] == dd;
            }
            return false;
        };
        // horizontal cuts
        for (int k = 1; k < m; k++) {
            long long sumt = pref_row[k];
            long long sumb = total - sumt;
            if (sumt == sumb) return true;
            if (sumt > sumb) {
                long long dif = sumt - sumb;
                if (can_rm(0, k - 1, 0, n - 1, dif)) return true;
            } else if (sumb > sumt) {
                long long dif = sumb - sumt;
                if (can_rm(k, m - 1, 0, n - 1, dif)) return true;
            }
        }
        // vertical cuts
        for (int k = 1; k < n; k++) {
            long long suml = pref_col[k];
            long long sumr = total - suml;
            if (suml == sumr) return true;
            if (suml > sumr) {
                long long dif = suml - sumr;
                if (can_rm(0, m - 1, 0, k - 1, dif)) return true;
            } else if (sumr > suml) {
                long long dif = sumr - suml;
                if (can_rm(0, m - 1, k, n - 1, dif)) return true;
            }
        }
        return false;
    }
};
# @lc code=end
