class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int ans = 0;
        const vector<pair<int,int>> dirs = {{1,1}, {1,-1}, {-1,1}, {-1,-1}};
        const vector<int> turn = {1,3,0,2};
        vector<vector<vector<vector<int>>>> dp(n, vector<vector<vector<int>>>(m, vector<vector<int>>(4, vector<int>(2,-1))));
        function<int(int,int,int,int,int)> dfs = [&](int x, int y, int dir, int turnUsed, int seqIdx) -> int {
            if (x<0 || y<0 || x>=n || y>=m) return 0;
            int expected = seqIdx == 0 ? 1 : ((seqIdx-1)%2==0 ? 2 : 0);
            if (grid[x][y] != expected) return 0;
            if (dp[x][y][dir][turnUsed] >= seqIdx) return 0;
            dp[x][y][dir][turnUsed] = seqIdx;
            int res = 1;
            res = max(res, 1 + dfs(x+dirs[dir].first, y+dirs[dir].second, dir, turnUsed, seqIdx+1));
            if (!turnUsed) {
                int newDir = turn[dir];
                res = max(res, 1 + dfs(x+dirs[newDir].first, y+dirs[newDir].second, newDir, 1, seqIdx+1));
            }
            return res;
        };
        for (int i=0;i<n;++i) {
            for (int j=0;j<m;++j) {
                if (grid[i][j]!=1) continue;
                for (int d=0;d<4;++d) {
                    ans = max(ans, dfs(i,j,d,0,0));
                }
            }
        }
        return ans>0?ans:0;
    }
};