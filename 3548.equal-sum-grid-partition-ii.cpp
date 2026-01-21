#
# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#
# @lc code=start
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i = 0; i < m - 1; i++) {
            if (checkHorizontalCut(grid, i)) return true;
        }
        
        for (int j = 0; j < n - 1; j++) {
            if (checkVerticalCut(grid, j)) return true;
        }
        
        return false;
    }
    
private:
    bool checkHorizontalCut(vector<vector<int>>& grid, int cutRow) {
        int m = grid.size(), n = grid[0].size();
        long long topSum = 0, bottomSum = 0;
        vector<pair<int,int>> topCells, bottomCells;
        
        for (int i = 0; i <= cutRow; i++) {
            for (int j = 0; j < n; j++) {
                topSum += grid[i][j];
                topCells.push_back({i, j});
            }
        }
        
        for (int i = cutRow + 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                bottomSum += grid[i][j];
                bottomCells.push_back({i, j});
            }
        }
        
        if (topSum == bottomSum) return true;
        
        if (topSum > bottomSum) {
            long long diff = topSum - bottomSum;
            for (auto [r, c] : topCells) {
                if (grid[r][c] == diff && isConnectedAfterRemoval(topCells, r, c)) return true;
            }
        }
        
        if (bottomSum > topSum) {
            long long diff = bottomSum - topSum;
            for (auto [r, c] : bottomCells) {
                if (grid[r][c] == diff && isConnectedAfterRemoval(bottomCells, r, c)) return true;
            }
        }
        
        return false;
    }
    
    bool checkVerticalCut(vector<vector<int>>& grid, int cutCol) {
        int m = grid.size(), n = grid[0].size();
        long long leftSum = 0, rightSum = 0;
        vector<pair<int,int>> leftCells, rightCells;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j <= cutCol; j++) {
                leftSum += grid[i][j];
                leftCells.push_back({i, j});
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = cutCol + 1; j < n; j++) {
                rightSum += grid[i][j];
                rightCells.push_back({i, j});
            }
        }
        
        if (leftSum == rightSum) return true;
        
        if (leftSum > rightSum) {
            long long diff = leftSum - rightSum;
            for (auto [r, c] : leftCells) {
                if (grid[r][c] == diff && isConnectedAfterRemoval(leftCells, r, c)) return true;
            }
        }
        
        if (rightSum > leftSum) {
            long long diff = rightSum - leftSum;
            for (auto [r, c] : rightCells) {
                if (grid[r][c] == diff && isConnectedAfterRemoval(rightCells, r, c)) return true;
            }
        }
        
        return false;
    }
    
    bool isConnectedAfterRemoval(vector<pair<int,int>>& cells, int removeR, int removeC) {
        set<pair<int,int>> cellSet;
        for (auto [r, c] : cells) {
            if (r != removeR || c != removeC) cellSet.insert({r, c});
        }
        
        if (cellSet.empty()) return false;
        
        set<pair<int,int>> visited;
        queue<pair<int,int>> q;
        q.push(*cellSet.begin());
        visited.insert(*cellSet.begin());
        
        int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};
        
        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k], ny = y + dy[k];
                if (cellSet.count({nx, ny}) && !visited.count({nx, ny})) {
                    visited.insert({nx, ny});
                    q.push({nx, ny});
                }
            }
        }
        
        return visited.size() == cellSet.size();
    }
};
# @lc code=end