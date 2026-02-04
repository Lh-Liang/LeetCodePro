#
# @lc app=leetcode id=3459 lang=cpp
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n == 0) return 0;
        int m = grid[0].size();
        if (m == 0) return 0;
        int maxLength = 0;
        
        const vector<pair<int, int>> directions = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        auto inBounds = [&](int x, int y) {
            return x >= 0 && x < n && y >= 0 && y < m;
        };
        
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(4, -1))); // DP table for memoization
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) { // Starting point must be '1'
                    for (int d = 0; d < directions.size(); ++d) {
                        maxLength = max(maxLength, explore(grid, dp, i, j, d));
                    }
                }
            }
        }
        return maxLength;
    }
    
private:
    int explore(vector<vector<int>>& grid, vector<vector<vector<int>>>& dp,
                int x, int y, int dirIndex) {
        const vector<pair<int,int>> directions = {{-1,-1}, {-1,1}, {1,-1}, {1,1}};
        queue<tuple<int,int,int,int>> q; // x,y,direction,length
        q.push({x + directions[dirIndex].first,
y + directions[dirIndex].second,
dirIndex,
grid[x][y] == 2 ? 2 : (grid[x][y] == 0 ? -2 : -3)});
dp[x][y][dirIndex] = grid[x][y] == ""return=""length=""");while(q.empty())versing:""q.pop()=""tuple<int,int>nextMove=""");}");return=""};};}");