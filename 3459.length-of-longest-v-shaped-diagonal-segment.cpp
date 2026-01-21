#
# @lc app=leetcode id=3459 lang=cpp
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> dpp(n * m * 8, 0);
        auto idx = [&](int r, int c, int d, int p) -> int {
            return ((r * m + c) * 4 + d) * 2 + p;
        };
        int dr[4] = {1, 1, -1, -1};
        int dc[4] = {1, -1, -1, 1};
        auto getv = [&](int r, int c, int d, int p) -> int {
            return dpp[idx(r, c, d, p)];
        };
        auto setv = [&](int r, int c, int d, int p, int val) {
            dpp[idx(r, c, d, p)] = val;
        };
        for (int d = 0; d < 4; ++d) {
            auto compute = [&](int r, int c) {
                for (int p = 0; p < 2; ++p) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                        setv(r, c, d, p, 0);
                        continue;
                    }
                    int need = (p == 0 ? 2 : 0);
                    if (grid[nr][nc] != need) {
                        setv(r, c, d, p, 0);
                        continue;
                    }
                    int np = 1 - p;
                    setv(r, c, d, p, 1 + getv(nr, nc, d, np));
                }
            };
            if (d == 0) {
                for (int r = n - 1; r >= 0; --r) {
                    for (int c = m - 1; c >= 0; --c) {
                        compute(r, c);
                    }
                }
            } else if (d == 1) {
                for (int r = n - 1; r >= 0; --r) {
                    for (int c = 0; c < m; ++c) {
                        compute(r, c);
                    }
                }
            } else if (d == 2) {
                for (int r = 0; r < n; ++r) {
                    for (int c = 0; c < m; ++c) {
                        compute(r, c);
                    }
                }
            } else {
                for (int r = 0; r < n; ++r) {
                    for (int c = m - 1; c >= 0; --c) {
                        compute(r, c);
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] != 1) continue;
                ans = max(ans, 1);
                for (int d = 0; d < 4; ++d) {
                    int steps = getv(i, j, d, 0);
                    ans = max(ans, 1 + steps);
                    int td = (d + 1) % 4;
                    int cr = i;
                    int cc = j;
                    int clen = 0;
                    while (clen < steps) {
                        cr += dr[d];
                        cc += dc[d];
                        ++clen;
                        int pturn = (clen % 2 == 0 ? 0 : 1);
                        int after = getv(cr, cc, td, pturn);
                        ans = max(ans, 1 + clen + after);
                    }
                }
            }
        }
        return ans;
    }
};
# @lc code=end