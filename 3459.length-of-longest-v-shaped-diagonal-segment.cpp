#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    int n, m;
    int memo[500][500][4][2];
    // Diagonal directions in clockwise order:
    // 0: (-1, -1) Top-Left
    // 1: (-1, 1)  Top-Right
    // 2: (1, 1)   Bottom-Right
    // 3: (1, -1)  Bottom-Left
    int dr[4] = {-1, -1, 1, 1};
    int dc[4] = {-1, 1, 1, -1};

    int solve(int r, int c, int dir, int turned, const vector<vector<int>>& grid) {
        if (memo[r][c][dir][turned] != -1) return memo[r][c][dir][turned];

        int current_val = grid[r][c];
        int next_val = 2 - current_val; // Toggles between 2 and 0
        int res = 1;

        // Option 1: Continue in the same diagonal direction
        int nr = r + dr[dir];
        int nc = c + dc[dir];
        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == next_val) {
            res = max(res, 1 + solve(nr, nc, dir, turned, grid));
        }

        // Option 2: Make a 90-degree clockwise turn (if not already turned)
        if (turned == 0) {
            int ndir = (dir + 1) % 4;
            int nnr = r + dr[ndir];
            int nnc = c + dc[ndir];
            if (nnr >= 0 && nnr < n && nnc >= 0 && nnc < m && grid[nnr][nnc] == next_val) {
                res = max(res, 1 + solve(nnr, nnc, ndir, 1, grid));
            }
        }

        return memo[r][c][dir][turned] = res;
    }

public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        
        memset(memo, -1, sizeof(memo));

        int max_len = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    max_len = max(max_len, 1);
                    // Try starting in all 4 diagonal directions
                    for (int d = 0; d < 4; ++d) {
                        int ni = i + dr[d];
                        int nj = j + dc[d];
                        // The sequence must start 1 -> 2
                        if (ni >= 0 && ni < n && nj >= 0 && nj < m && grid[ni][nj] == 2) {
                            max_len = max(max_len, 1 + solve(ni, nj, d, 0, grid));
                        }
                    }
                }
            }
        }
        return max_len;
    }
};