#
# @lc app=leetcode id=3459 lang=cpp
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution {
public:
    int n, m;
    int memo[505][505][4][2];
    // Directions: 0: SE, 1: SW, 2: NW, 3: NE (Clockwise order)
    int dr[4] = {1, 1, -1, -1};
    int dc[4] = {1, -1, -1, 1};

    // Check if coordinates are within grid bounds
    bool isValid(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < m;
    }

    int dfs(vector<vector<int>>& grid, int r, int c, int dir, int turned) {
        if (memo[r][c][dir][turned] != -1) {
            return memo[r][c][dir][turned];
        }

        int currentVal = grid[r][c];
        int targetNext = (currentVal == 2) ? 0 : 2;
        
        int maxLength = 0;

        // Option 1: Continue in the same direction
        int nr = r + dr[dir];
        int nc = c + dc[dir];
        
        if (isValid(nr, nc) && grid[nr][nc] == targetNext) {
            maxLength = max(maxLength, 1 + dfs(grid, nr, nc, dir, turned));
        }

        // Option 2: Turn 90 degrees clockwise (only if haven't turned yet)
        if (turned == 0) {
            int newDir = (dir + 1) % 4;
            int tr = r + dr[newDir];
            int tc = c + dc[newDir];
            
            if (isValid(tr, tc) && grid[tr][tc] == targetNext) {
                maxLength = max(maxLength, 1 + dfs(grid, tr, tc, newDir, 1));
            }
        }

        return memo[r][c][dir][turned] = maxLength;
    }

    int lenOfVDiagonal(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        
        // Initialize memoization table with -1
        // Using memset is faster/easier for C-style arrays
        // Size: 505 * 505 * 4 * 2 * sizeof(int) is roughly 8MB, perfectly fine.
        memset(memo, -1, sizeof(memo));

        int maxLen = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    // A segment of length at least 1 exists.
                    maxLen = max(maxLen, 1);
                    
                    // Try starting in all 4 diagonal directions looking for the next '2'
                    for (int d = 0; d < 4; ++d) {
                        int ni = i + dr[d];
                        int nj = j + dc[d];
                        
                        if (isValid(ni, nj) && grid[ni][nj] == 2) {
                            // Length is 1 (current '1') + 1 (next '2') + whatever follows
                            maxLen = max(maxLen, 2 + dfs(grid, ni, nj, d, 0));
                        }
                    }
                }
            }
        }

        return maxLen;
    }
};
# @lc code=end