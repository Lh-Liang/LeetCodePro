#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3459 lang=cpp
//
// [3459] Length of Longest V-Shaped Diagonal Segment
//

// @lc code=start
class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = (int)grid.size();
        int m = (int)grid[0].size();
        auto id = [m](int i, int j) { return i * m + j; };
        auto inside = [n, m](int i, int j) {
            return i >= 0 && i < n && j >= 0 && j < m;
        };

        // Clockwise order: NE -> SE -> SW -> NW
        const int D = 4;
        int dx[D] = {-1,  1,  1, -1};
        int dy[D] = { 1,  1, -1, -1};

        int N = n * m;

        // dpFrom1: for each direction, store best odd/even length ending at cell.
        vector<vector<int>> endOdd(D, vector<int>(N, 0));
        vector<vector<int>> endEven(D, vector<int>(N, 0));

        int ans = 0;

        // Build dpFrom1 for each direction
        for (int d = 0; d < D; d++) {
            // To use prev = (i - dx, j - dy), we need prev row computed before.
            // If dx==1 => prev row is i-1 => traverse i increasing.
            // If dx==-1 => prev row is i+1 => traverse i decreasing.
            int istart = (dx[d] == 1 ? 0 : n - 1);
            int iend   = (dx[d] == 1 ? n : -1);
            int istep  = (dx[d] == 1 ? 1 : -1);

            for (int i = istart; i != iend; i += istep) {
                for (int j = 0; j < m; j++) {
                    int cur = id(i, j);
                    int odd = 0, even = 0;
                    int val = grid[i][j];

                    if (val == 1) {
                        odd = 1;
                    }

                    int pi = i - dx[d];
                    int pj = j - dy[d];
                    if (inside(pi, pj)) {
                        int prev = id(pi, pj);
                        int pOdd = endOdd[d][prev];
                        int pEven = endEven[d][prev];
                        if (val == 2 && pOdd > 0) {
                            even = max(even, pOdd + 1);
                        }
                        if (val == 0 && pEven > 0) {
                            odd = max(odd, pEven + 1);
                        }
                    }

                    endOdd[d][cur] = odd;
                    endEven[d][cur] = even;
                    ans = max(ans, max(odd, even));
                }
            }
        }

        // altStart[d][t][cell]: longest alt 0/2 sequence along dir d starting at cell
        // with expected value t (0->0, 1->2).
        vector<vector<vector<int>>> altStart(D, vector<vector<int>>(2, vector<int>(N, 0)));

        for (int d = 0; d < D; d++) {
            // Transition uses next = (i + dx, j + dy). We need next computed before.
            // If dx==1 => next row is i+1 => traverse i decreasing.
            // If dx==-1 => next row is i-1 => traverse i increasing.
            int istart = (dx[d] == 1 ? n - 1 : 0);
            int iend   = (dx[d] == 1 ? -1 : n);
            int istep  = (dx[d] == 1 ? -1 : 1);

            for (int i = istart; i != iend; i += istep) {
                for (int j = 0; j < m; j++) {
                    int cur = id(i, j);
                    int ni = i + dx[d];
                    int nj = j + dy[d];
                    int nxt = inside(ni, nj) ? id(ni, nj) : -1;

                    for (int t = 0; t <= 1; t++) {
                        int expected = (t == 0 ? 0 : 2);
                        if (grid[i][j] != expected) {
                            altStart[d][t][cur] = 0;
                        } else {
                            int add = 0;
                            if (nxt != -1) add = altStart[d][1 - t][nxt];
                            altStart[d][t][cur] = 1 + add;
                        }
                    }
                }
            }
        }

        // Combine for V-shapes: first leg in d, second in clockwise(d)
        for (int d = 0; d < D; d++) {
            int d2 = (d + 1) % D;
            int dx2 = dx[d2], dy2 = dy[d2];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int cur = id(i, j);
                    int ni = i + dx2;
                    int nj = j + dy2;
                    int nxt = inside(ni, nj) ? id(ni, nj) : -1;

                    int Lodd = endOdd[d][cur];
                    if (Lodd > 0) {
                        // Next expected after odd length is 2
                        int L2 = (nxt == -1 ? 0 : altStart[d2][1][nxt]);
                        ans = max(ans, Lodd + L2);
                    }

                    int Leven = endEven[d][cur];
                    if (Leven > 0) {
                        // Next expected after even length is 0
                        int L2 = (nxt == -1 ? 0 : altStart[d2][0][nxt]);
                        ans = max(ans, Leven + L2);
                    }
                }
            }
        }

        return ans;
    }
};
// @lc code=end
