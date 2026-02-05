#
# @lc app=leetcode id=3459 lang=cpp
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#
# @lc code=start
class Solution {
public:
    int n, m;
    vector<vector<int>> grid;
    // Directions: [dr, dc] for the four diagonals
    const vector<pair<int, int>> dirs = { {1,1}, {1,-1}, {-1,1}, {-1,-1} };
    // For each direction, the index of its clockwise 90-degree turn
    const vector<int> clockwise = {1,3,0,2};
    // dp cache: r, c, dir, turn_used, parity (0: expect 2, 1: expect 0)
    int dp[500][500][4][2][2];
    
    int dfs(int r, int c, int dir, bool turned, int parity) {
        if (r<0 || r>=n || c<0 || c>=m) return 0;
        int expected = parity ? 0 : 2;
        if (grid[r][c] != expected) return 0;
        int &res = dp[r][c][dir][turned][parity];
        if (res != -1) return res;
        int len = 1;
        // Continue in same direction
        len = max(len, 1 + dfs(r + dirs[dir].first, c + dirs[dir].second, dir, turned, parity ^ 1));
        // If not turned yet, try turn
        if (!turned) {
            int ndir = clockwise[dir];
            len = max(len, 1 + dfs(r + dirs[ndir].first, c + dirs[ndir].second, ndir, 1, parity ^ 1));
        }
        return res = len;
    }
    int lenOfVDiagonal(vector<vector<int>>& grid_) {
        grid = grid_;
        n = grid.size();
        m = grid[0].size();
        memset(dp, -1, sizeof(dp));
        int ans = 0;
        for (int r=0; r<n; ++r) {
            for (int c=0; c<m; ++c) {
                if (grid[r][c] == 1) {
                    for (int d=0; d<4; ++d) {
                        int nr = r + dirs[d].first, nc = c + dirs[d].second;
                        // Start dfs only if next cell exists and matches the expected first (2)
                        if (nr>=0 && nr<n && nc>=0 && nc<m && grid[nr][nc]==2) {
                            ans = max(ans, 2 + dfs(nr + dirs[d].first, nc + dirs[d].second, d, 0, 1));
                        } else {
                            ans = max(ans, 1);
                        }
                    }
                }
            }
        }
        return ans;
    }
};
# @lc code=end